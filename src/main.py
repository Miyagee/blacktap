from filestream import FileStream
from receiver import Receiver
from sensors import Sensors
from geometry import Geometry
from distributor import Distributor
from time import sleep
from gui import GUI
import numpy as np
import threading
import time

class Main:
    def __init__(self):
        self._socket_address = 'data_stream.sock'
        self._stream = FileStream("downtown-east2_turn_sigs.json",
                self._socket_address)
        self._receiver = Receiver(self._socket_address)
        self._geo_listen = Geometry()
        self._frequency = 15

        self._send_frequency = 1
        self._distributor = Distributor('upload_stream.sock',
                self._send_frequency)
        self._gui = GUI()

        t = threading.Thread(target=self._mainloop)
        t.daemon = True
        t.start()

        s = threading.Thread(target=self._sender)
        s.daemon = True
        s.start()

        self._gui.mainloop()

    def _mainloop(self):
        while True:
            sleep(1 / self._frequency)
            if Geometry._pos is not None:
                self._gui.set_coords(*Geometry._pos)
            if Geometry._marker is not None:
                self._gui.set_marker(Geometry._marker)
    def _sender(self):
        while True:
            self._distributor.send()
            sleep(1 / self._send_frequency)


if __name__ == '__main__':
    m = Main()
