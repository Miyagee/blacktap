# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

import json
import time
import requests
import tkinter
import numpy as np
import googlemaps
from sys import argv
from threading import Thread, RLock
from collections import deque, defaultdict as dd
from PIL import ImageFile, ImageTk, Image


class FileReader(Thread):

    #Constructor
        def __init__(self, url):
            super(FileReader, self).__init__()
            self.daemon = True

            self.url = url
            self.results = dd(list)
            self.lock = RLock()

            self.speed_up = 4.0


        def change_speed_by(self, k):
            self.speed_up *= k

        def get_speed(self):
            return self.speed_up

        #Simulate time delay between input	
        def sleeper(self, cur_timestamp, old_timestamp):
            if cur_timestamp > old_timestamp:
                time.sleep((cur_timestamp-old_timestamp) / self.speed_up)
            return cur_timestamp

        #Opens and read the file with date input
        def run(self):

            data = []
            old_timestamp = None

            with open(self.url) as f:
                data.extend(f.readlines())

            for i in range(len(data)):
                json_data = json.loads(data[i])

                if old_timestamp is None: # Initial case
                    old_timestamp = json_data["timestamp"]
                old_timestamp = self.sleeper(json_data["timestamp"], old_timestamp)

                with self.lock:
                    self.results[json_data['name']].append( (json_data["value"], json_data["timestamp"]) )

        #Getter to get all results
        def get_data(self):
            return self.lock, self.results

class GUI(tkinter.Tk):
    def __init__(self):
        super(GUI, self).__init__()

        self.title("Trip Simulator")
        self.img = Image.open("Googlemapslogo2014.png")
        self.img = self.img.convert("RGB")

        self.photo_image = ImageTk.PhotoImage(self.img)
        self.canvas = tkinter.Canvas(self, width = 500, height = 500)
        self.canvas.create_image(250, 250, image = self.photo_image)
        self.canvas.pack()

        self.stream = FileReader("downtown-east2.json")
        self.stream.start()

        self.last_position = None
        self.center = np.array([250, 250]) # Center of screen
        self.marker = (self.center[0] - 5, self.center[1] - 5,
                self.center[0] + 5, self.center[1] - 5,
                self.center[0] + 5, self.center[1] + 5,
                self.center[0] - 5, self.center[1] + 5)
        self.update_image()

        self.bind("<Key>", self.handle_key_press)

        self.cli = googlemaps.Client(key="AIzaSyCehm2J69ZTy8Z-10FwDDgVZb5l0k0PFEE")
        self.turning = {} # Dictionary to be filled with points and a timer, for marking turns
        self.street_address = None # Current street address (derived from coords)
        self.coord_mem = deque() # Remember few last coords for the turn line
        self.coord_mem_cap = 5 # capacity = 5
        
        self.mainloop()

    def handle_key_press(self, key):
        if key.keycode == 1769515: # pluss-tegn
            self.stream.change_speed_by(1.5)  # speed up stream
        elif key.keycode == 2883629: # minus-tegn
            self.stream.change_speed_by(1 / 1.5) # slow down stream

    def update_image(self):
        lock, data = self.stream.get_data()
        with lock:
            if len(data['longitude']) > 0 and len(data['latitude']) > 0:
                lat = data['latitude'][-1][0]
                lng = data['longitude'][-1][0]

                do_update = True

                if self.last_position is None:
                    self.last_position = (lat, lng)
                elif self.last_position[0] != lat or self.last_position[1] != lng:
                    r = [lng - self.last_position[1], lat - self.last_position[0]] # retningsvektor
                    ortog = [1, 1] # orthogonal vektor
                    if r[0] == 0:
                        ortog[1] = 0
                    elif r[1] == 0:
                        ortog[0] = 0
                    else:
                        ortog[1] = -r[0] / r[1]
                    r = np.array(r)             # Linear algebra vector
                    ortog = np.array(ortog)

                    r = r * 20 / np.linalg.norm(r)              # Normaliserer til lengde 20
                    ortog = ortog * 20 / np.linalg.norm(ortog)

                    r[1] *= -1
                    ortog[1] *= -1

                    self.marker = list(self.center - 0.5*r - ortog*0.3) + list(self.center + r*0.5) + list(self.center - 0.5*r + ortog*0.3)
                    self.last_position = (lat, lng)

                    # START TURNING LOGIC
                    self.coord_mem.append( (lat, lng))
                    if self.coord_mem_cap < len(self.coord_mem):
                        self.coord_mem.popleft()

                    address = self.street_address # in case of failure
                    try:
                        response = self.cli.reverse_geocode((lat, lng), result_type = "route")
                        response = response[0]
                        for line in response['address_components']:
                            if 'route' in line['types']:
                                address = line['long_name']
                                break
                    except (e):
                        print(e)

                    if self.street_address is None:
                        self.street_address = address
                    elif address != self.street_address:
                        self.turning = {'time' : time.time(), 'coords' : list(self.coord_mem)}
                        self.street_address = address
                        print("TURNING")

                    if self.turning: # Evaluate as bool
                        if len(self.turning['coords']) > 2 and 0.0003 < \
                        np.linalg.norm(np.array(self.turning['coords'][-1] - np.array(self.turning['coords'][0]))):
                            ##5 < time.time() - self.turning['time']: # Mark only for two seconds
                            self.turning = {}
                        else:
                            self.turning['coords'].append( (lat, lng) )
                else:
                    do_update = False

                if do_update:
                    #start = time.time()
                    self.img = self.fetch_img(data['latitude'][-1][0], data['longitude'][-1][0])
                    #print("Downloaded image in " + format((time.time() - start) * 1000, '.1f') + " ms.")
                    self.photo_image = ImageTk.PhotoImage(self.img)
                    
                self.canvas.create_image(250, 250, image = self.photo_image)

                self.canvas.create_polygon(self.marker, fill="blue")

                self.canvas.create_rectangle(0, 0, 150, 80, fill="white")
                self.canvas.create_text((10, 5), anchor = "nw", text="Play speed: " + \
                        format(self.stream.get_speed(), '.1f')+"x")
                
                speed = speed_limit = None
                if len(data['vehicle_speed']) > 0:
                    speed = data['vehicle_speed'][-1][0]*1.6
                if len(data['speed_limit']) > 0:
                    speed_limit = data['speed_limit'][-1][0]

                self.canvas.create_text((10, 20), anchor = "nw", text="Velocity: " + \
                        (format(speed, '.1f') + " km/h" if speed is not None else "?"))

                self.canvas.create_text((10, 35), anchor = "nw", text="Speed limit: " + \
                        (format(speed_limit, '.1f') if speed_limit is not None else "?"))
                
                speeding = "Unknown"
                color = "black"
                if speed is not None and speed_limit is not None:
                    if speed <= speed_limit:
                        speeding = "No"
                        color = "green"
                    else:
                        speeding = "Yes"
                        color = "red"
                        
                self.canvas.create_text((10, 50), anchor = "nw", text="Speeding: " + speeding, fill = color)

        self.after(200, self.update_image)

    def fetch_img(self, lat, lng):
        req = self.build_request(lat, lng)
        response = requests.get(req)

        if response.ok:
            parser = ImageFile.Parser()
            parser.feed(response.content)
            image = parser.close()
            return image
        else:
            raise Exception("Could not fetch map image")

    def build_request(self, lat, lng):
        col = "%3A" # URL encoding for :
        pip = "%7C"
        s = "https://maps.googleapis.com/maps/api/staticmap?" + \
                    "key=AIzaSyCehm2J69ZTy8Z-10FwDDgVZb5l0k0PFEE" + "&" + \
                    "center="+str(lat)+","+str(lng) + "&" + \
                    "zoom=17" + "&" + \
                    "size=500x500"
        if self.turning:
            s += "&path=color"+col+"0x0000ffff"+pip+"weight"+col+"5"+ \
                    pip.join(str(tup[0])+","+str(tup[1]) for tup in self.turning['coords'])

        return s

if __name__ == "__main__":
    gui = GUI()
