from sensors import Sensors
import json
from queue import Queue
from geometry import Geometry
from distributor import Distributor
from time import sleep
import numpy as np
import threading

class Green(threading.Thread):
    """This class is used to calculate current fuel usage, if the user is driving green and some other stuff."""

    def __init__(self, sleep_duration, event):
        print('Initializing')
        self.event = event
        threading.Thread.__init__(self, target=None, args=None)
        self.queue = Distributor.analyzes
        self.sleep_duration = sleep_duration
        self.lastGearEvaluate = ('none', 'asd')

        # Start our thread!
        print('Start!')
        self.start()

    def _evaluateGearChange(self, engine_speed, current_gear, vehicle_speed, timestamp):
        print('Engine speed: %r\t Current gear: %r\t Vehicle speed: %r' % (engine_speed, current_gear, vehicle_speed))
        if vehicle_speed > 1:
            if engine_speed > 2000:
                self.event.direction = 'up'
                if 'up' != self.lastGearEvaluate[0]:
                    self.lastGearEvaluate = ('up', timestamp)
            elif engine_speed < 1000 and current_gear != 'first':
                self.event.direction = 'down'
                if 'down' != self.lastGearEvaluate[0]:
                    self.lastGearEvaluate = ('down', timestamp)
            else:
                if 'none' != self.lastGearEvaluate[0]:
                    #In this case we are going from a state where we should gear up/down to a state where the current gear is good.
                    print({'name':'gear_change_suggestion', 'direction':self.lastGearEvaluate[0], 'timestamp':self.lastGearEvaluate[1], 'end_time':timestamp})
                    self.queue.put({'name':'gear_change_suggestion', 'direction':self.lastGearEvaluate[0], 'timestamp':self.lastGearEvaluate[1], 'end_time':timestamp})
                    self.lastGearEvaluate = ('none', timestamp)

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
                self._evaluateGearChange(engine_speed_data[-1].get('value'), gear_data[-1].get('value'), vehicle_speed_data[-1].get('value'), vehicle_speed_data[-1].get('timestamp'))

            fuel_diff = fuel_data[-1].get('value') - fuel_data[-2].get('value') #difference between the two last measured fuel levels
            distance_diff = distance_data[-1].get('value') - distance_data[-2].get('value')

            if distance_diff > 0:
                fuel_usage_per_km = fuel_diff / distance_diff
            else:
                fuel_usage_per_km = 0
            self.queue.put({'name':'fuel_usage_per_10km', 'value':fuel_usage_per_km*10, 'timestamp':fuel_data[-1].get('timestamp')})


if __name__ == '__main__':
    with open("./downtown-east2.json") as f:
        lines = f.readlines()

    for e in lines[100:]:
        Sensors(Sensors.insert_data, json.loads(e))

    g = Green(1)
    g.run()
