from tkinter import *
from maps import Maps
from PIL import Image, ImageTk, ImageDraw, ImageFont
from vibratingbox import VibratingBox
import numpy as np

class GUI(Tk):

    def __init__(self):
        super(GUI, self).__init__()
        self._width = 550
        self._height = 900
        self.title("Blacktap")
        self._canvas = Canvas(self, width=self._width, height=self._height, bg
                = "#F0F0F0")
        self._canvas.pack()

        self._turn_signal_sym = VibratingBox((100, 175),
                Image.open("resources/turn_signal_symbol.jpg"), self._canvas)
        self._thumbs_down_sym = VibratingBox((450, 175),
                Image.open("resources/thumbs_down_symbol.jpg"), self._canvas)
        self._thumbs_up_sym = VibratingBox((450, 175),
                Image.open("resources/thumbs_up_symbol.jpg"), self._canvas)
        self._marker = None

        self.set_speed_limit(120)
        self._turn_signal_sym.set_vibrate(10)
        self._speed_limit_sym.set_vibrate(5)
        self._thumbs_up_sym.set_vibrate(3)
        self._thumbs = True # thumbs up

        self._map = Maps()
        self._map_img = None
        self._map_tk = None
        self._coords = None
        self.set_coords(40.77192, -73.953773)

        self._update()

    def set_coords(self, lat, lng):
        self._coords = (lat, lng)

    def set_thumbs(self, val):
        self._thumbs = val

    def set_speed_limit(self, speed):
        img = Image.open("resources/speed_limit_symbol.jpg")
        draw = ImageDraw.Draw(img)
        speed = str(speed)
        if len(speed) == 2:
            draw.text((40, 50), str(speed), font =
                    ImageFont.truetype('resources/sansation.ttf',
                60), fill ="black")
        elif len(speed) == 3:
            draw.text((35, 50), str(speed), font =
                    ImageFont.truetype('resources/sansation.ttf',
                55), fill ="black")
        self._speed_limit_sym = VibratingBox((275, 175), img, self._canvas)

    def set_marker(self, marker):
        self._marker = np.matrix([[500, 0], [0, 500]]) * marker

    def _update(self):
        self._canvas.delete("all")

        if self._coords is not None:
            self._map_img = Image.new("RGB", (502, 402), color="black") # frame
            mapimg = self._map[self._coords[0],
                    self._coords[1]].crop((0, 50, 500, 450))
            self._map_img.paste(mapimg, (1,1))
            self._map_tk = ImageTk.PhotoImage(self._map_img)
            self._canvas.create_image( (275, 475), image=self._map_tk)
            if self._marker is not None:
                points = list(np.asarray(np.reshape(self._marker,
                    self._marker.size))[0])
                points = [e+225 if i % 2 else e +25 for i, e in  enumerate(points)]
                self._canvas.create_polygon(points, fill="blue")

        self._turn_signal_sym.draw()
        self._speed_limit_sym.draw()
        if self._thumbs:
            self._thumbs_up_sym.draw()
        else:
            self._thumbs_down_sym.draw()
        self.after(20, self._update)

if __name__ == '__main__':
    G = GUI()