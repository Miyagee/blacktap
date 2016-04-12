import threading
import time
from sensors import Sensors
from distributor import Distributor


class AggressiveAnalyzer(threading.Thread):
    def __init__(self, event):
        super(AggressiveAnalyzer, self).__init__()

        self._event = event
        self._frequency = 2  # times per second
        self._start_time = None
        self._end_time = None
        self._points = []
        self.start()

    def run(self):
        """
        Available data:
         + accelerator_pedal_position
            - percentage
         + brake_pedal_status
            - boolean
         + engine_speed
            - 0 - 16382 (rpm)
         + torque_at_transmission
            - Nm
         + vehicle_speed
            - km/h

         - fuel_consumed_since_restart
         - fuel_level
         - odometer
         - steering_wheel_angle
         - transmission_gear_position
        """
        while True:
            time.sleep(1.0 / self._frequency)
            acc_ped_pos, brake_pedal_status, engine_speed = [], [], []
            Sensors.get_last(lambda obj: obj['name'] == 'accelerator_pedal_position', acc_ped_pos)
            acc_ped_pos = acc_ped_pos[0]['value'] if acc_ped_pos else None
            if acc_ped_pos:
                print("Accelerator pedal status {}".format(acc_ped_pos))
                if self.is_driving_aggressively(acc_ped_pos):
                    self._event.set()

                    if self._start_time is None:
                        self._start_time = pos[0]['timestamp']
                elif self._start_time:
                    self._end_time = pos[0]['timestamp']
                    # self._send()

    def is_driving_aggressively(self, acc_ped_pos):
        return acc_ped_pos > 25




