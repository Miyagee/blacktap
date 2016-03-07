# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

import json
import time
import requests
import tkinter
import numpy as np
import googlemaps
import os
from sys import argv
from threading import Thread, RLock
from collections import deque, defaultdict as dd
from PIL import ImageFile, ImageTk, Image
from math import cos, pi

from maps import Maps


class FileReader(Thread):

    # Constructor
    def __init__(self, url):
        super(FileReader, self).__init__()
        self.daemon = True

        self.url = url
        self.results = dd(list)
        self.lock = RLock()

        self.speed_up = 1.0

        #For creating data subsets for test making:
        self.record = False
        self.record_buffer = []
        self.record_index = 1
        self.filename_prefix = "records/record"
        self.rewind = None

    def change_speed_by(self, k):
        self.speed_up *= k

    def get_speed(self):
        return self.speed_up

    # Simulate time delay between input
    def sleeper(self, cur_timestamp, old_timestamp):
        if cur_timestamp > old_timestamp:
            time.sleep((cur_timestamp - old_timestamp) / self.speed_up)
        return cur_timestamp

    # Opens and read the file with date input
    def run(self):

        data = []
        old_timestamp = None

        with open(self.url) as f:
            data.extend(f.readlines())
        i = 0
        while i < (len(data)):
            json_data = json.loads(data[i])

            if self.record:
                self.record_buffer.append(data[i])
            elif not self.record and self.record_buffer:
                filename = self.filename_prefix + str(self.record_index)
                self.record_index += 1
                while os.path.isfile(filename):
                    filename = self.filename_prefix + str(self.record_index)
                    self.record_index += 1

                open(filename, "w").write("".join(self.record_buffer))
                self.record_buffer = []
            elif self.rewind:
                i -= 1
                json_data = json.loads(data[i])
                now = json_data['timestamp']
                while 0 < i and json_data['timestamp'] > now - self.rewind:
                    i -= 1
                    json_data = json.loads(data[i])
                    self.results[json_data['name']].pop()
                old_timestamp = None
                self.rewind = None

            if old_timestamp is None: # Initial case
                old_timestamp = json_data["timestamp"]
            old_timestamp = self.sleeper(json_data["timestamp"], old_timestamp)

            with self.lock:
                self.results[json_data['name']].append( (json_data["value"], json_data["timestamp"]) )
            i += 1

    # Getter to get all results
    def get_data(self):
        return self.lock, self.results


class GUI(tkinter.Tk):
    def __init__(self, *files):

        super(GUI, self).__init__()

        self.title("Trip Simulator")
        self.img = Image.open("Googlemapslogo2014.png")
        self.img = self.img.convert("RGB")

        self.photo_image = ImageTk.PhotoImage(self.img)
        self.canvas = tkinter.Canvas(self, width=500, height=500)
        self.canvas.create_image(250, 250, image=self.photo_image)
        self.canvas.pack()


        self.last_position = None
        self.last_speed = None
        self.last_direction = None
        self.inter_lat = None
        self.inter_lng = None
        self.center = np.array([250, 250]) # Center of screen

        self.bind("<Key>", self.handle_key_press)

        self.cli = googlemaps.Client(key="AIzaSyCehm2J69ZTy8Z-10FwDDgVZb5l0k0PFEE")
        self.coord_mem_cap = 5 # capacity = 5
        
        self.test_files = list(files)
        self.stream = None

        self.map = Maps()
        self.update_stream()
        self.update_image() # Periodic tasks
        self.turning = {}  # Dictionary to be filled with points and a timer, for marking turns
        self.street_address = None  # Current street address (derived from coords)
        self.coord_mem = deque()  # Remember few last coords for the turn line
        self.coord_mem_cap = 5  # capacity = 5

        self.mainloop()

    def handle_key_press(self, key):
        if key.keycode == 1769515:  # pluss-tegn
            self.stream.change_speed_by(1.5)  # speed up stream
        elif key.keycode == 2883629: # minus-tegn
            self.stream.change_speed_by(1 / 1.5) # slow down stream
        elif key.keycode == 983154:
            self.stream.record = not self.stream.record
        elif key.keycode == 720994:
            self.stream.rewind = 30
            self.reset_data()

    def update_stream(self):
        if len(self.test_files) and (self.stream is None or not self.stream.is_alive()):
            self.stream = FileReader(self.test_files.pop())
            self.active = True
            self.reset_data()
            self.stream.start()
        elif not self.stream.is_alive():
            self.img = Image.open("Googlemapslogo2014.png")
            self.img = self.img.convert("RGB")

            self.photo_image = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(250, 250, image = self.photo_image)
            self.active = False

        self.after(1000, self.update_stream)

    def reset_data(self):
            self.last_position = None
            self.street_address = None

            self.turning = {} # Dictionary to be filled with points and a timer, for marking turns
            self.street_address = None # Current street address (derived from coords)
            self.coord_mem = deque() # Remember few last coords for the turn line

    def update_image(self):
        if not self.active:
            return

        lock, data = self.stream.get_data()
        with lock:
            lat = data['latitude'][-1][0] if len(data['latitude']) > 0 else None
            lng = data['longitude'][-1][0] if len(data['longitude']) > 0 else None

            speed = 1.6 * data['vehicle_speed'][-1][0] if len(data['vehicle_speed']) > 0 else None
            speed_limit = data['speed_limit'][-1][0] if len(data['speed_limit']) > 0 else None
        del data # delete reference

        if lat is not None and lng is not None:

            if self.last_position is None:
                self.last_position = (lat, lng)
                self.interpolate_time = time.time()
            elif self.last_position[0] != lat or self.last_position[1] != lng:
                self.last_direction = (lat - self.last_position[0], lng - self.last_position[1])
                self.last_position = (lat, lng)
                self.interpolate_time = time.time()
                self.inter_lat, self.inter_lng = lat, lng
                #self.check_turning(lat, lng)
            else:
                if self.last_speed is not None and speed is not None and self.last_direction is not None:
                    self.interpolate(speed)
                    lat, lng = self.inter_lat, self.inter_lng

            marker = self.make_marker()
            self.last_speed = speed
            self.redraw_elements(lat, lng, speed, speed_limit, marker)

        self.after(50, self.update_image)

    def interpolate(self, speed):
        r = np.array(self.last_direction)
        r /= np.linalg.norm(r)
        r *= 0.5 / 3.6 / 2.5 * (self.last_speed + speed) * (time.time() - self.interpolate_time) * self.stream.get_speed() # 2.5 is a magic constant :-(

        self.interpolate_time = time.time()
        self.inter_lat += r[0] / 111111
        self.inter_lng += r[1] / (111111 * cos(self.inter_lat / 360 * 2*pi))

    def make_marker(self):
        if self.last_direction == None:
            return (self.center[0] - 5, self.center[1] - 5,
                    self.center[0] + 5, self.center[1] - 5,
                    self.center[0] + 5, self.center[1] + 5,
                    self.center[0] - 5, self.center[1] + 5)

        r = self.last_direction[::-1]#[lng - self.last_position[1], lat - self.last_position[0]] # retningsvektor
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

        return list(self.center - 0.5*r - ortog*0.3) + list(self.center + r*0.5) + list(self.center - 0.5*r + ortog*0.3)

    def check_turning(self, lat, lng):
        self.coord_mem.append( (lat, lng))
        if self.coord_mem_cap < len(self.coord_mem):
            self.coord_mem.popleft()

        if self.turning: # Evaluate as bool
            if len(self.turning['coords']) > 2 and 0.0003 < \
                    np.linalg.norm(np.array(self.turning['coords'][-1] - np.array(self.turning['coords'][0]))) \
                    and 4 < time.time() - self.turning['time']:
                self.turning = {}
            else:
                self.turning['coords'].append( (lat, lng) )
            return

        address = self.street_address
        try: # Haults (stucks) after quota of 2500 lookups per day.
            response = self.cli.reverse_geocode((lat, lng), result_type = "route")
            response = response[0]
            for line in response['address_components']:
                if 'route' in line['types']:
                    address = line['long_name']
                    break
        except Exception as e:
            print(e)

        if self.street_address is None:
            self.street_address = address
        elif address != self.street_address:
            self.turning = {'time' : time.time(), 'coords' : list(self.coord_mem)}
            self.street_address = address
            print("TURNING")

    def redraw_elements(self, lat, lng, speed, speed_limit, marker):
        self.canvas.delete("all")
        self.img = self.map[lat, lng]
        self.photo_image = ImageTk.PhotoImage(self.img)
            
        self.canvas.create_image(250, 250, image = self.photo_image)

        self.canvas.create_polygon(marker, fill="blue")

        if self.stream.record:
            self.canvas.create_oval(490, 15, 500, 5, fill = "red")


        self.canvas.create_rectangle(0, 0, 150, 80, fill="white")

        self.canvas.create_text((10, 5), anchor = "nw", text="Play speed: " + \
                format(self.stream.get_speed(), '.1f')+"x")
        
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
        col = "%3A"  # URL encoding for :
        pip = "%7C"
        s = "https://maps.googleapis.com/maps/api/staticmap?" + \
            "key=AIzaSyCehm2J69ZTy8Z-10FwDDgVZb5l0k0PFEE" + "&" + \
            "center=" + str(lat) + "," + str(lng) + "&" + \
            "zoom=17" + "&" + \
            "size=500x500"
        if self.turning:
            s += "&path=color" + col + "0x0000ffff" + pip + "weight" + col + "5" + \
                pip.join(str(tup[0]) + "," + str(tup[1]) for tup in self.turning['coords'])

        print(s)
        return s

if __name__ == "__main__":
    gui = GUI("downtown-east2.json")
    #gui = GUI(*["records/"+filename for filename in os.listdir("records/")])
