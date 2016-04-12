from tkinter import *
from maps import Maps
from PIL import Image, ImageTk, ImageDraw, ImageFont
from vibratingbox import VibratingBox
from evaluatebox import EvaluateBox
import numpy as np
import time

class GUI(Tk):

    def __init__(self):
        super(GUI, self).__init__()
        self._width = 550
        self._height = 900

        self.title("Blacktap")
        self._canvas = Canvas(self, width=self._width, height=self._height, bg
                = "#F0F0F0")
        self._canvas.pack()

        self._speed_limit_sym = VibratingBox((275, 175),
                Image.open("resources/speed_limit_symbol.jpg"), self._canvas)
        self._turn_signal_sym = VibratingBox((100, 175),
                Image.open("resources/turn_signal_symbol.jpg"), self._canvas)
        self._evaluate_box = EvaluateBox((450, 175), self._canvas)
        #self._thumbs_down_sym = VibratingBox((450, 175),
        #        Image.open("resources/thumbs_down_symbol.jpg"), self._canvas)
        #self._thumbs_up_sym = VibratingBox((450, 175),
        #        Image.open("resources/thumbs_up_symbol.jpg"), self._canvas)
        self._marker = None
        self._marker_id = None

        self._thumbs = True # thumbs up

        self._marker_matrix = np.matrix([
            [500, 0, 26],
            [0, 500, 226],
            [0, 0, 1]
            ])


        self._map = Maps()
        self._map_img = None
        self._map_tk = None
        self._map_id = None
        self._coords = None

        self._update_map()
        self._update_symbols()


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
        self._speed_limit_sym._image = img
        self._speed_limit_sym._image_tk = ImageTk.PhotoImage(self._speed_limit_sym._image)
        self._canvas.itemconfig(self._speed_limit_sym._id, image =
                self._speed_limit_sym._image_tk)

    def set_marker(self, marker):
        self._marker = list(np.array((self._marker_matrix *
            marker)[:2:].flatten('F')[0])[0])

    def _update_map(self):

        self._map_img = Image.new("RGB", (502, 402), color="black") # frame
        if self._coords is not None:
            mapimg = self._map[self._coords[0],
                    self._coords[1]].crop((0, 50, 500, 450))
        else:
            mapimg = Image.open("resources/logo.jpg")
        self._map_img.paste(mapimg, (1,1))
        self._map_tk = ImageTk.PhotoImage(self._map_img)
        if self._map_id is None:
            self._map_id = self._canvas.create_image( (275, 475), image=self._map_tk)
        else:
            self._canvas.itemconfig(self._map_id, image = self._map_tk)
        if self._marker is not None:
            if self._marker_id is not None:
                self._canvas.delete(self._marker_id)
            self._marker_id = self._canvas.create_polygon(self._marker, fill="blue")

        self.after(100, self._update_map)

    def _update_symbols(self):
        self._turn_signal_sym.draw()
        self._speed_limit_sym.draw()
        self._evaluate_box.draw()
        #if self._thumbs:
        #    self._thumbs_up_sym.draw()
        #else:
        #    self._thumbs_down_sym.draw()
        self.after(20, self._update_symbols)

if __name__ == '__main__':
    G = GUI()
