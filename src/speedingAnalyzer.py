import threading
import time
from sensors import Sensors

class SpeedingAnalyzer(threading.Thread):
    def __init__(self, event):
        super(SpeedingAnalyzer, self).__init__()

        self._event = event
        self._frequency = 2

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
                self._event.speed_limit = speed_lim
                if vehic_speed and self.is_speeding(vehic_speed, speed_lim):
                    self._event.set()
                    self._event.speeding_percentage = (vehic_speed - speed_lim) / speed_lim

    def is_speeding(self, velocity, limit):
        return velocity >= limit + 10
