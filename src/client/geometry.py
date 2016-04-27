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
    _time = None

    _frequency = 10
    _inter_pos = None
    _fix_a = 0

    def __init__(self):
        super(Geometry, self).__init__(daemon=True)
        self._last_time = None
        self._last_stamp = None
        self._step_size = 1
        self._p0 = None
        self._p1 = None
        self._dir = None
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
            Sensors.get_data(lambda obj: obj['name'] == 'latitude',
                             pos_lats, 3)
            Sensors.get_data(lambda obj: obj['name'] == 'longitude',
                             pos_lngs, 3)

            if len(pos_lats) < 3 or len(pos_lngs) < 3:
                continue
            p0, p1, p2 = ((a['value'], b['value'])
                          for a, b in zip(pos_lats, pos_lngs))
            t0, t1, t2 = (pos_lats[i]['timestamp'] for i in range(3))

            Geometry._time = t2
            Geometry._pos = p2
            Geometry._r = Geometry._make_r(p1, p2)
            Geometry._v = Geometry._r / (t2 - t1)
            Geometry._a = (Geometry._v - Geometry._make_r(p0, p1) /
                           (t1 - t0)) / ((t2 + t1) / 2 - (t1 + t0) / 2)

            if self._last_stamp != t2:
                if self._last_time is None:
                    self._last_time = time.time()
                alph = 0.7
                self.step_size = alph * self._step_size + \
                    (1 - alph) * (time.time() - self._last_time)

                if Geometry._inter_pos is None:
                    Geometry._inter_pos = p2

                # Stabilize
                self._dir = 0.3 * (np.array(p2) - Geometry._inter_pos) + 0.7 * (
                    self._dir if self._dir is not None else np.array(p2) - Geometry._inter_pos)

                self._last_stamp = t2
                self._last_update_time = time.time()
                self._last_time = time.time()

            k = (time.time() - self._last_update_time) / self._step_size
            self._last_update_time = time.time()
            Geometry._inter_pos = list(self._dir * k + Geometry._inter_pos)

            Geometry._build_marker()

    def _make_r(start, end):
        dlat = end[0] - start[0]
        dlng = end[1] - start[1]

        return -np.array([dlng * 111111 * cos(end[0] /
                                              360 * 2 * pi), dlat * 111111])

    def _r_to_coords(r):
        return -np.array([r[0] / 111111, r[1] / (111111 *
                                                 cos(Geometry._pos[0] * pi / 180))][::-1])

    def _build_marker():
        r = np.append(Geometry._r, 0)  # copy

        center = np.array([0.5, 0.5, 1])
        if (Geometry._marker is None and (r is None or np.linalg.norm(r) == 0)):
            r = np.array([0., 1., 0.])
        elif (r is None or np.linalg.norm(r) == 0):
            return

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
