from filestream import FileStream
from receiver import Receiver
from geometry import Geometry
from distributor import Distributor
from time import sleep
from gui import GUI
from sensors import Sensors
from green import Green
from analyzers.turnSignalAnalyzer import TurnSignalAnalyzer
from analyzers.speedingAnalyzer import SpeedingAnalyzer
import numpy as np
import threading
import time
from queue import Queue

class Main:
    def __init__(self):
        self._socket_address = 'data_stream.sock'
        self._stream = FileStream("../../gen_data/downtown-east2_only_turn_sigs_speed_lims.json", self._socket_address)
        self._receiver = Receiver(self._socket_address)
        self._geo_listen = Geometry()
        self._frequency = 15

        self._send_frequency = 1
        self._speed_limit = None
        self._speed_time = None

        self._gui = None

        self._forgot_signals_event = threading.Event()
        self._speeding_event = threading.Event()
        self._speeding_event.speed_limit = None
        self._last_turn_forget = None
        self._turn_analyzer = TurnSignalAnalyzer(self._forgot_signals_event)
        self._speeding_analyzer = SpeedingAnalyzer(self._speeding_event)
        self._green = Green(Queue(),1)

        t = threading.Thread(target=self._mainloop)
        t.daemon = True
        t.start()

        self._gui = GUI()

        #self._distributor = Distributor('upload_stream.sock',self._send_frequency)
        #s = threading.Thread(target=self._sender)
        #s.daemon = True
        #s.start()

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

            if self._speed_limit != self._speeding_event.speed_limit:
                self._speed_limit = self._speeding_event.speed_limit
                self._gui.set_speed_limit(self._speed_limit)
            if self._speeding_event.is_set():
                self._gui._speed_limit_sym.set_vibrate(10 * self._speeding_event.speeding_percentage)
                self._speeding_event.clear()
                self._speed_time = time.time()
            elif self._speed_time is not None and time.time()-self._speed_time > 2:
                self._gui._speed_limit_sym.set_vibrate(0)


    def _sender(self):
        while True:
            self._distributor.send()
            sleep(1 / self._send_frequency)

if __name__ == '__main__':
    m = Main()
