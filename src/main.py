from filestream import FileStream
from receiver import Receiver
from geometry import Geometry
from distributor import Distributor
from time import sleep
from gui import GUI
from sensors import Sensors
from turnSignalAnalyzer import TurnSignalAnalyzer
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
        self._speed_limit = None

        self._gui = None

        self._forgot_signals_event = threading.Event()
        self._last_turn_forget = None
        self._turn_analyzer = TurnSignalAnalyzer(self._forgot_signals_event)

        t = threading.Thread(target=self._mainloop)
        t.daemon = True
        t.start()

        self._gui = GUI()

        self._distributor = Distributor('upload_stream.sock',self._send_frequency)
        s = threading.Thread(target=self._sender)
        s.daemon = True
        s.start()

        self._gui.mainloop()

    def _mainloop(self):
        while True:
            sleep(1 / self._frequency)
            if self._gui is None:
                continue
            if Geometry._pos is not None:
                if Geometry._inter_pos:
                    self._gui.set_coords(*Geometry._inter_pos)
                else:
                    self._gui.set_coords(*Geometry._pos)
            if Geometry._marker is not None:
                self._gui.set_marker(Geometry._marker)

            if self._forgot_signals_event.is_set():
                self._last_turn_forget = time.time()
                self._gui._turn_signal_sym.set_vibrate(10)
                self._forgot_signals_event.clear()
            if self._last_turn_forget is not None and time.time() - self._last_turn_forget > 3:
                self._gui._turn_signal_sym.set_vibrate(0)

            data = []
            Sensors.get_last(lambda obj : obj['name'] == 'speed_limit', data)
            speeds = []
            Sensors.get_last(lambda obj : obj['name'] == 'vehicle_speed',
                    speeds)
            if data and data[0]['value'] != self._speed_limit:
                self._gui.set_speed_limit(data[0]['value'])
                self._speed_limit = data[0]['value']
            if speeds and self._speed_limit and 1.8*speeds[0]['value'] > 1.1 * self._speed_limit:
                self._gui._speed_limit_sym.set_vibrate(12 * (1.8*speeds[0]['value'] -
                        self._speed_limit) / self._speed_limit)
                print(12 * (1.8*speeds[0]['value'] - self._speed_limit) / self._speed_limit)

    def _sender(self):
        while True:
            self._distributor.send()
            sleep(1 / self._send_frequency)

if __name__ == '__main__':
    m = Main()
