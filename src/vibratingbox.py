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

            old_vy = self._vy
            self._vy += self._gravity * dt
            self._dy += self._vy * dt

            if self._dy > 0:
                self._vy = -0.8 * old_vy
                self._dy = 0

        self._canvas.create_image( (self._position[0], self._position[1] + \
            self._dy), image=self._image_tk)


    def set_vibrate(self, value):
        self._vibrate_value = value
        self._time = None

if __name__ == '__main__':

    def update(root, canvas, vb):
        canvas.delete("all")
        vb.draw()
        root.after(20, lambda : update(root, canvas, vb))

    root = Tk()
    canvas = Canvas(root, height = 500, width = 500)
    im = Image.open("s.png")
    im = im.convert("RGB")
    canvas.pack()

    vb = VibratingBox((250, 250), im, canvas)
    vb.set_vibrate(10)
    root.after(20, lambda : update(root, canvas, vb))
    root.mainloop()
