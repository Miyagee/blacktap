from sensors import Sensors
from geometry import Geometry
from distributor import Distributor
import threading
import time
import googlemaps
import logging

class TurnSignalAnalyzer(threading.Thread):

    def __init__(self, event):
        super(TurnSignalAnalyzer, self).__init__()

        self._event = event
        self._frequency = 1
        self._cli = googlemaps.Client(key="AIzaSyCehm2J69ZTy8Z-10FwDDgVZb5l0k0PFEE")
        self._street_address = None
        self._last_turn = None

        self.start()

    def run(self):
        while True:
            time.sleep(1.0 / self._frequency)
            wheel_rot = []
            if Geometry._pos is None:
                continue
            lat, lng = Geometry._pos
            Sensors.get_last(lambda obj : obj['name'] == 'steering_wheel_angle',  wheel_rot, max_age = 1)
            if wheel_rot:
                wheel_rot = wheel_rot[0]['value']
                if abs(wheel_rot) > 75 or self._street_address is None:
                    self._last_turn = time.time()

            if self._last_turn is not None and time.time() - self._last_turn < 3:
                address = self._street_address
                try: # Haults (stucks) after quota of 2500 lookups per day.
                    response = self._cli.reverse_geocode((lat, lng), result_type = "route")
                    response = response[0]
                    for line in response['address_components']:
                        if 'route' in line['types']:
                            address = line['long_name']
                            break
                except Exception as e:
                    logging.debug(e)

                if self._street_address is None:
                    self._street_address = address
                elif address != self._street_address:
                    self._street_address = address
                    self._event.set()
                    Distributor.analyzes.put( {'position' : [lat, lng], 'type' : 'forgot_turn_signals'} )
