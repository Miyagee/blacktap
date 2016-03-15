from sensors import Sensors
from functools import reduce
import socket
import json


class Distributor(object):

    def __init__(self, address, frequency):

        self._sock = socket.socket(AF_UNIX, SOCK_STREAM)
        self._socket_address = address

        self._socket.connect(self._address)
        self._period = 1 / frequency

        self._datas = [  # name, function tuple
                ('accelerator_pedal_position', self._average),
                ('brake_pedal_status', self._average),
                ('door_status', self._last),
                ('engine_speed', self._average),
                ('fuel_consumed_since_restart', self._last),
                ('fuel_level', self._last),
                ('gear_lever_position', self._last),
                ('headlamp_status', self._last),
                ('high_beam_status', self._last),
                ('ignition_status', self._last),
                ('latitude', self._last),
                ('latitude', self._last),
                ('longitude', self._last),
                ('longitude', self._last),
                ('odometer', self._last),
                ('parking_brake_status', self._any),
                ('speed_limit', self._any),
                ('transmission_gear_position', self._last),
                ('turn_signal', self._any),
                ('vehicle_speed', self._average),
                ('windshield_wiper_status', self._any)]

    def send(self):
        paylooad = [e[1](e[0]) for e in self._datas]

        self._socket.send(json.dumps(payload))

    def _average(self, name):
        data = []
        Sensors.get_data(lambda obj : obj['name'] == name, data, max_age =
                self._period)
        return sum(elem['value'] for elem in data) / len(data)

    def _last(self, name):
        data = []
        Sensors.get_last(lambda obj : obj['name'] == name, data, max_age =
                self._period)
        if data:
            return data[0]['value']
        else:
            return None

    def _any(self, name):
        data = []
        Sensors.get_data(lambda obj : obj['name'] == name, data, max_age =
                self._period)
        return reduce(lambda a, b : a['value'] or b['value'], data, False)
