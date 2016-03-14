import threading
import numpy as np
from sensors import Sensors
from math import cos, pi
import time

class Geometry(threading.Thread):

    _pos = None
    _r = None
    _v = None
    _a = None
    _marker = None
    _alt_v = None

    _frequency = 20
    _last_time = None

    def __init__(self):
        super(Geometry, self).__init__()
        self.start()

    def pos():
        return Geometry._pos

    def r():
        return Geometry._r

    def v():
        return Geometry._v

    def a():
        return Geometry._a

    def marker():
        return Geometry._marker

    def run(self):
        while True:
            time.sleep(1 / Geometry._frequency)

            pos_lats = []
            pos_lngs = []
            Sensors(Sensors.get_data, lambda obj : obj['name'] == 'latitude',
                    pos_lats, 3).join()
            Sensors(Sensors.get_data, lambda obj : obj['name'] == 'longitude',
                    pos_lngs, 3).join()

            if len(pos_lats) < 3 or len(pos_lngs) < 3:
                continue
            p0, p1, p2 = ((a['value'], b['value']) for a,b in zip(pos_lats, pos_lngs))
            t1, t2=(pos_lats[i]['timestamp']-pos_lats[i-1]['timestamp'] for i in [1,2])

            Geometry._pos = p2
            Geometry._r = Geometry._make_r(p1, p2)
            Geometry._v = Geometry._r / t2
            Geometry._a = (Geometry._v - (Geometry._make_r(p0, p1) / t1)) / t2

            if np.linalg.norm(Geometry._r) != 0:
                Geometry._build_marker()


    def _make_r(start, end):
        dlat = end[0] - start[0]
        dlng = end[1] - start[1]

        return np.array([dlat * 111111, dlng * 111111 * cos(end[0] / 360 * 2 * pi)])

    def _build_marker():
        r = np.array(-Geometry._r)  # copy

        center = np.array([0.5, 0.5])
        if r is None:
            Geometry._marker = np.transpose([center + np.array([e1*0.05, e2*0.05])
                for e1 in [-1, 1] for e2 in [-1, 1]])
        else:
            orth = np.cross(np.array(list(r) + [0]), np.array([0, 0, 1]))[:2]

            r[1] *= -1  # y-direction reversed on screen
            orth[1] *= -1

            r *= 0.025 / np.linalg.norm(r)  # normalize length
            orth *= 0.020 / np.linalg.norm(orth)

            Geometry._marker = np.transpose([
                center - r - orth,
                center + r,
                center - r + orth])
