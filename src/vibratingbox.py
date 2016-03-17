from tkinter import Tk, Canvas
from PIL import Image, ImageTk
import time

class VibratingBox:

    def __init__(self, position, image, canvas):
        self._canvas = canvas
        self._image = image
        self._image_tk = ImageTk.PhotoImage(self._image)
        self._position = position
        self._vibrate_value = 0
        self._dy = 0
        self._vy = 0
        self._time = None
        self._id = None

        self._gravity = 800

    def draw(self):
        if -self._dy + self._vy**2 < 0.01:
            self._time = time.time()
            self._dy = 0
            self._vy = -self._vibrate_value*30

        if self._time is None:
            self._time = time.time()
        else:
            dt = time.time() - self._time
            self._time = time.time()

            old_dy = self._dy
            old_vy = self._vy

            self._vy += self._gravity * dt
            self._dy += self._vy * dt

            if self._dy > 0:
                self._vy = -0.8 * old_vy
                self._dy = 0

        if self._id is None:
            self._id = self._canvas.create_image( (self._position[0], self._position[1] + \
                self._dy), image=self._image_tk)
        else:
            self._canvas.move(self._id, 0, self._dy - old_dy)  # takes dx, dy arguments

    def set_vibrate(self, value):
        self._vibrate_value = value
        self._time = None
