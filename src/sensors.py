import threading
import logging

logging.basicConfig(level=logging.WARNING, format='[%(threadName)-10s] %(message)s')


class Sensors(threading.Thread):
    """Class making data available for other objects"""

    # Static variables
    _lock = threading.Condition(threading.Lock())  # data lock
    _data = []  # JSON objects, sorted by timestamp
    _readers = 0  # current readers count

    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

    @staticmethod
    def _add_reader():
        with Sensors._lock:
            Sensors._readers += 1

    @staticmethod
    def _remove_reader():
        with Sensors._lock:
            Sensors._readers -= 1
            if not Sensors._readers:
                Sensors._lock.notify_all()

    @staticmethod
    def insert_data(obj):
        """Inserts a JSON-object into data"""
        with Sensors._lock:
            while Sensors._readers > 0:
                Sensors._lock.wait()
            Sensors._data.append(obj)

    @staticmethod
    def get_last(pred, ret, max_age=10**10):
        """Get the last data object satisfying the predicate 'pred'"""
        Sensors._add_reader()
        if not Sensors._data:
            return
        before = Sensors._data[-1]["timestamp"] - max_age
        for obj in reversed(Sensors._data):
            if obj["timestamp"] < before:
                break
            elif pred(obj):
                ret.append(obj)
                break
        Sensors._remove_reader()

    @staticmethod
    def get_data(pred, ret, num_limit=10**10, max_age=10**10):
        """Adds all data which satisfies the predicate 'pred' in the max_age last seconds to 'ret'"""
        Sensors._add_reader()
        if not Sensors._data:
            return
        before = Sensors._data[-1]["timestamp"] - max_age
        objs = []
        for obj in reversed(Sensors._data):
            if num_limit == len(objs) or obj["timestamp"] < before:
                break
            elif pred(obj):
                objs.append(obj)
        Sensors._remove_reader()
        ret.extend(objs)


def test():
    with open("./downtown-east2.json") as f:
        lines = f.readlines()

    in_data = lines[:10]
    Sensors(Sensors.insert_data, in_data)

    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])
    Sensors(Sensors.get_data, lambda x: False, [])


if __name__ == '__main__':
    test()
