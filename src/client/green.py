from sensors import Sensors
import json
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

    def run(self):
        sleep(5*self.sleep_duration)
        fuel_data = []
        distance_data = []

        Sensors.get_last(lambda obj: obj['name'] == 'fuel_consumed_since_restart', fuel_data)
        Sensors.get_last(lambda obj: obj['name'] == 'odometer', distance_data)

        while True:
            sleep(self.sleep_duration)
            Sensors.get_last(lambda obj: obj['name'] == 'fuel_consumed_since_restart', fuel_data)
            Sensors.get_last(lambda obj: obj['name'] == 'odometer', distance_data)

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

    g = Green([], 1)
    g.run()
