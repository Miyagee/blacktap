import threading
from receiver import Receiver
import numpy as np
from sensors import Sensors
from math import cos, pi
import time
import sys  # remove

class Geometry(threading.Thread):

    _pos = None
    _r = None
    _v = None
    _a = None
    _marker = None

    _frequency = 10
    _inter_pos = None

    def __init__(self):
        super(Geometry, self).__init__()
        self._time_mem = (None, None)
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
            Sensors.get_data(lambda obj : obj['name'] == 'latitude',
                    pos_lats, 3)
            Sensors.get_data(lambda obj : obj['name'] == 'longitude',
                    pos_lngs, 3)

            if len(pos_lats) < 3 or len(pos_lngs) < 3:
                continue
            p0, p1, p2 = ((a['value'], b['value']) for a,b in zip(pos_lats, pos_lngs))
            t0, t1, t2= (pos_lats[i]['timestamp'] for i in range(3))

            Geometry._pos = p2
            Geometry._r = Geometry._make_r(p1, p2)
            Geometry._v = Geometry._r / (t2 - t1)
            Geometry._a = (Geometry._v - Geometry._make_r(p0, p1) / (t1-t0)) / ((t2+t1)/2 - (t1+t0)/2)

            if self._time_mem[0] != pos_lngs[-1]['timestamp']:
                self._time_mem = (pos_lngs[-1]['timestamp'], time.time())

            dt = time.time() - self._time_mem[1]
            if Geometry._a is not None:
                #Geometry._inter_pos = list(np.array(p2) + Geometry._r_to_coords(dt*Geometry._v + 0.5*dt**2*Geometry._a))
                p0, p1, p2 = (np.array(p) for p in (p0, p1, p2))
                Geometry._inter_pos = list(p2 + (p2-p1)/(t2-t1)*dt + 0.5* ((p2-p1)/(t2-t1) - (p1-p0)/(t1-t0)) / ((t2+t1)/2 - (t1+t0)/2)*dt**2)

            Geometry._build_marker()

    def _make_r(start, end):
        dlat = end[0] - start[0]
        dlng = end[1] - start[1]

        return -np.array([dlng * 111111 * cos(end[0] / 360 * 2 * pi), dlat * 111111])

    def _r_to_coords(r):
        return -np.array([r[0] / 111111, r[1] / (111111 * cos(Geometry._pos[0] *
            pi/180))][::-1])

    def _build_marker():
        r = np.append(Geometry._r, 0)  # copy

        center = np.array([0.5, 0.5, 1])
        if r is None or np.linalg.norm(r) == 0:
            Geometry._marker = np.transpose([center + 0.013*np.array([e1, e2*e1, 0])
                for e1 in [-1, 1] for e2 in [-1, 1]])
        else:
            orth = np.cross(r, np.array([0, 0, 1]))

            r[1] *= -1  # y-direction reversed on screen
            orth[1] *= -1
            orth[2] = 0

            r *= 0.020 / np.linalg.norm(r)  # normalize length
            orth *= 0.013 / np.linalg.norm(orth)

            Geometry._marker = np.transpose([
                center - r - orth,
                center + r,
                center - r + orth])
