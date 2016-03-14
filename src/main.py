from filestream import FileStream
from receiver import Receiver
from sensors import Sensors
from geometry import Geometry
from time import sleep
from gui import GUI
import numpy as np
import threading
import time

class Main:
    def __init__(self):
        self._socket_address = 'data_stream.sock'
        self._stream = FileStream('downtown-east2.json', self._socket_address)
        self._receiver = Receiver(self._socket_address)
        self._geo_listen = Geometry()
        self._frequency = 15

        self._gui = GUI()

        t = threading.Thread(target=self._mainloop)
        t.daemon = True
        t.start()

        self._gui.mainloop()

    def _mainloop(self):
        while True:
            sleep(1 / self._frequency)
            if Geometry._pos is not None:
                self._gui.set_coords(*Geometry._pos)
            if Geometry._marker is not None:
                self._gui.set_marker(Geometry._marker)

if __name__ == '__main__':
    m = Main()
