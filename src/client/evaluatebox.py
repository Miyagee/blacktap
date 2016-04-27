from tkinter import Tk, Canvas, HIDDEN, NORMAL
from PIL import Image, ImageTk
import math
import time


class EvaluateBox:
    GOOD = 0
    BAD = 1
    GEAR_UP = 3
    GEAR_DOWN = 4

    def __init__(self, position, canvas):
        self._canvas = canvas
        self._good = ImageTk.PhotoImage(
            Image.open("src/client/resources/thumbs_up_symbol.jpg"))

        self._bad = ImageTk.PhotoImage(
            Image.open("src/client/resources/thumbs_down_symbol.jpg"))

        self._gear_up = ImageTk.PhotoImage(
            Image.open("src/client/resources/gear_up.jpg"))

        self._gear_down = ImageTk.PhotoImage(
            Image.open("src/client/resources/gear_down.jpg"))

        self._value = EvaluateBox.GOOD
        self._position = position

        self._symbol_widget = self._canvas.create_image(
            position, image=self._good)

        self._previous = None

    def draw(self):
        if self._previous == self._value:
            return

        if self._value == EvaluateBox.GOOD:
            self._canvas.itemconfig(self._symbol_widget, image=self._good)
        elif self._value == EvaluateBox.BAD:
            self._canvas.itemconfig(self._symbol_widget, image=self._bad)
        elif self._value == EvaluateBox.GEAR_UP:
            self._canvas.itemconfig(self._symbol_widget, image=self._gear_up)
        elif self._value == EvaluateBox.GEAR_DOWN:
            self._canvas.itemconfig(self._symbol_widget, image=self._gear_down)
        self._previous = self._value

    def set_value(self, value):
        self._value = value
