from threading import Thread
from PIL import Image, ImageFile, ImageTk
import requests
from time import sleep
import tkinter


class Maps:

    def __init__(self):
        self.pieces = {}
        self.pending = set()

        self.dlat = 0.004063
        self.dlng = 0.005365

    def __getitem__(self, pos):
        lat, lng = pos

        ind_lat = lat // self.dlat
        ind_lng = lng // self.dlng
        part_lat = (lat % self.dlat) / self.dlat
        part_lng = (lng % self.dlng) / self.dlng

        result = Image.new("RGB", (500, 500), "white")
        im1 = self.get_part(ind_lat, ind_lng)
        im2 = self.get_part(ind_lat + 1, ind_lng)
        im3 = self.get_part(ind_lat, ind_lng + 1)
        im4 = self.get_part(ind_lat + 1, ind_lng + 1)

        result.paste(im1, (int(-part_lng * 500), int(part_lat * 500)))
        result.paste(im2, (int(-part_lng * 500), int(-(1 - part_lat) * 500)))
        result.paste(im3, (int((1 - part_lng) * 500), int(part_lat * 500)))
        result.paste(im4, (int((1 - part_lng) * 500),
                           int(-(1 - part_lat) * 500)))

        return result

    def get_part(self, ind_lat, ind_lng):
        index = (ind_lat, ind_lng)
        if index in self.pieces:
            return self.pieces[index]
        else:
            if index not in self.pending:
                self.pending.add(index)
                T = Thread(target=self.download, args=index)
                T.daemon = True
                T.start()
            return Image.new("RGB", (500, 500), "white")

    def download(self, ind_lat, ind_lng):
        lat, lng = ind_lat * self.dlat, ind_lng * self.dlng
        response = requests.get(
            "https://maps.googleapis.com/maps/api/staticmap?" +
            "key=AIzaSyCehm2J69ZTy8Z-10FwDDgVZb5l0k0PFEE&" +
            "center=" + str(lat) + "," + str(lng) + "&" +
            "zoom=17&size=500x500")
        parser = ImageFile.Parser()
        parser.feed(response.content)
        self.pieces[(ind_lat, ind_lng)] = parser.close()
        self.pending.remove((ind_lat, ind_lng))


class tester(tkinter.Tk):

    def __init__(self):
        super(tester, self).__init__()

        self.map = Maps()

        self.lat = 63.4176044
        self.lng = 10.4126962

        self.canvas = tkinter.Canvas(self, width=500, height=500)
        self.canvas.pack()

        self.bind("<Key>", self.handle_key_press)

        self.update()
        self.mainloop()

    def handle_key_press(self, key):
        if key.keycode == 8124162:
            self.lng -= 0.05 * self.map.dlng
        elif key.keycode == 8320768:
            self.lat += 0.05 * self.map.dlat
        elif key.keycode == 8189699:
            self.lng += 0.05 * self.map.dlng
        elif key.keycode == 8255233:
            self.lat -= 0.05 * self.map.dlat

    def update(self):
        self.canvas.delete("all")
        self.photo_img = ImageTk.PhotoImage(self.map[self.lat, self.lng])
        self.canvas.create_image(250, 250, image=self.photo_img)
        self.after(50, self.update)

if __name__ == '__main__':
    test = tester()
