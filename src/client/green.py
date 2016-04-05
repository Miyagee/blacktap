from sensors import Sensors
import json
from queue import Queue
from geometry import Geometry
from time import sleep
import numpy as np
import threading

class Green(threading.Thread):
    """This class is used to calculate current fuel usage, if the user is driving green and some other stuff."""

    def __init__(self, queue, sleep_duration):
        print('Initializing')
        threading.Thread.__init__(self, target=None, args=None)
        self.queue = queue
        self.sleep_duration = sleep_duration

        # Start our thread!
        print('Start!')
        self.start()

    def _evaluateGearChange(self, engine_speed, current_gear, vehicle_speed):
        print('Engine speed: %r\t Current gear: %r\t Vehicle speed: %r' % (engine_speed, current_gear, vehicle_speed))
        if vehicle_speed > 1:
            if engine_speed > 2000:
                self.queue.put(('gear_change_suggestion', 'up'))
            elif engine_speed < 1000:
                self.queue.put(('gear_change_suggestion', 'down'))

    def run(self):
        sleep(5*self.sleep_duration)
        fuel_data = []
        distance_data = []
        engine_speed_data = []
        gear_data = []
        vehicle_speed_data = []

        Sensors.get_last(lambda obj: obj['name'] == 'fuel_consumed_since_restart', fuel_data)
        Sensors.get_last(lambda obj: obj['name'] == 'odometer', distance_data)

        while True:
            sleep(self.sleep_duration)
            Sensors.get_last(lambda obj: obj['name'] == 'fuel_consumed_since_restart', fuel_data)
            Sensors.get_last(lambda obj: obj['name'] == 'odometer', distance_data)
            Sensors.get_last(lambda obj: obj['name'] == 'engine_speed', engine_speed_data)
            Sensors.get_last(lambda obj: obj['name'] == 'transmission_gear_position', gear_data)
            Sensors.get_last(lambda obj: obj['name'] == 'vehicle_speed', vehicle_speed_data)
            if gear_data and engine_speed_data and vehicle_speed_data:
                self._evaluateGearChange(engine_speed_data[-1].get('value'), gear_data[-1].get('value'), vehicle_speed_data[-1].get('value'))

            fuel_diff = fuel_data[-1].get('value') - fuel_data[-2].get('value') #difference between the two last measured fuel levels
            distance_diff = distance_data[-1].get('value') - distance_data[-2].get('value')

            if distance_diff > 0:
                fuel_usage_per_km = fuel_diff / distance_diff
            else:
                fuel_usage_per_km = 0
            self.queue.put(('fuel_usage_per_10km', fuel_usage_per_km*10))


if __name__ == '__main__':
    with open("./downtown-east2.json") as f:
        lines = f.readlines()

    for e in lines[100:]:
        Sensors(Sensors.insert_data, json.loads(e))

    g = Green(Queue(), 1)
    g.run()
