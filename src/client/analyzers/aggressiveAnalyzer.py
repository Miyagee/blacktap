import threading
import time
from sensors import Sensors
from distributor import Distributor
from geometry import Geometry


class AggressiveAnalyzer(threading.Thread):

    def __init__(self, event):
        super(AggressiveAnalyzer, self).__init__(daemon=True)

        self._event = event
        self._frequency = 2  # times per second
        self._start_time = None
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
            acc_ped_pos = []
            vehicle_speed = []
            Sensors.get_last(
                lambda obj: obj['name'] == 'accelerator_pedal_position',
                acc_ped_pos)
            Sensors.get_last(
                lambda obj: obj['name'] == 'vehicle_speed',
                vehicle_speed)

            acc_ped_pos = acc_ped_pos[0] if acc_ped_pos else None
            vehicle_speed = vehicle_speed[0] if vehicle_speed else None
            if acc_ped_pos is not None and vehicle_speed is not None:
                timestamp = acc_ped_pos["timestamp"]
                ped_pos = acc_ped_pos['value']
                speed = vehicle_speed['value']
                print("Accelerator pedal status {}".format(ped_pos))
                print("Acceleration: {}".format(self.get_acceleration()))
                if self.is_driving_aggressively(ped_pos):
                    print("AGGRESSIVE!")
                    self._event.set()
                    if self._start_time is None:
                        self._start_time = acc_ped_pos['timestamp']
                    self._send()
                self._points.append((timestamp, ped_pos, speed))

    def is_driving_aggressively(self, acc_ped_pos):
        return abs(self.get_acceleration()) > 1.0 or acc_ped_pos > 25

    def get_acceleration(self):
        if len(self._points) < 2:
            return 0
        num_points = min(5, len(self._points))
        points = self._points[-num_points:]
        timestamps, acc_ped, speed = zip(*points)
        try:
            acceleration = (speed[-1] - speed[0]) / 3.6 / \
                (float(timestamps[-1]) - float(timestamps[0]))
        except ZeroDivisionError:
            acceleration = 0
        return acceleration

    def _send(self):
        Distributor.analyzes.put({
            'name': 'aggressive',
            'value': 1,
            'timestamp': Geometry._time
        })

        self._start_time = None
        self._points = []
