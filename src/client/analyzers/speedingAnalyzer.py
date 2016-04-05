import threading
import time
from sensors import Sensors
from distributor import Distributor

class SpeedingAnalyzer(threading.Thread):
    def __init__(self, event):
        super(SpeedingAnalyzer, self).__init__()

        self._event = event
        self._frequency = 2

        self._velocities = []
        self._points = []
        self._start_time = None
        self._end_time = None
        self.start()

    def run(self):
        while True:
            time.sleep(1.0 / self._frequency)
            speed_lim, vehic_speed = [], []
            Sensors.get_last(lambda obj : obj['name'] == 'speed_limit', speed_lim)
            Sensors.get_last(lambda obj : obj['name'] == 'vehicle_speed', vehic_speed)

            speed_lim = speed_lim[0]['value'] if speed_lim else None
            vehic_speed = vehic_speed[0]['value']*1.8 if vehic_speed else None
            if speed_lim:

                pos = []
                Sensors.get_last(lambda obj : obj['name'] == 'latitude', pos)
                Sensors.get_last(lambda obj : obj['name'] == 'longitude', pos)

                if vehic_speed and self.is_speeding(vehic_speed, speed_lim):
                    self._event.set()
                    self._event.speeding_percentage = (vehic_speed - speed_lim) / speed_lim

                    if self._velocities and self._event.speed_limit and speed_lim != self._event.speed_limit:
                        self._send()

                    if not self._start_time:
                        self._start_time = pos[0]['timestamp']
                    self._velocities.append(vehic_speed)
                    self._points.append(list(map(lambda obj : obj['value'], pos)))

                elif vehic_speed and self._start_time: # No longing speeding, has things to send
                    self._end_time = pos[0]['timestamp']
                    self._send()

                self._event.speed_limit = speed_lim

    def _send(self):
        Distributor.analyzes.put( {
            'type' : 'speeding',
            'points' : self._points,
            'start time' : self._start_time,
            'end time' : self._end_time,
            'max speed' : max(self._velocities),
            'avg speed' : sum(self._velocities) / len(self._velocities),
            'speed limit' : self._event.speed_limit })
        print(Distributor.analyzes.get(), "\n\n") # REMOVE ME PL0X

        self._start_time = None
        self._end_time = None
        self._velocities.clear()
        self._points.clear()

    def is_speeding(self, velocity, limit):
        return velocity >= limit + 10
