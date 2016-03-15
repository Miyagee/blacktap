import threading
import logging
import json

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
        """Inserts a list of JSON-strings into data"""
        with Sensors._lock:
            logging.debug("Aquired lock")
            while Sensors._readers > 0:
                logging.debug("Waiting on readers")
                Sensors._lock.wait()


            logging.debug("Detected no readers")
            Sensors._data.append(obj)
            logging.debug("Data written")
            logging.debug("Releasing lock")

    @staticmethod
    def get_last(pred, ret):
        """Get the last data object satisfying the predicate 'pred'"""
        Sensors._add_reader()
        for obj in reversed(Sensors._data):
            if pred(obj):
                ret.append(obj)
                break
        Sensors._remove_reader()

    @staticmethod
    def get_data(pred, ret, num_limit = 10**10):
        """Adds all data which satisfies the predicate 'pred' after timestamp 'after' to 'ret'"""
        Sensors._add_reader()
        logging.debug("reading data")
        objs = []
        for obj in reversed(Sensors._data):
            if num_limit == len(objs):
                break
            elif pred(obj):
                objs.append(obj)
        logging.debug("finished reading data")
        Sensors._remove_reader()
        ret.extend(objs)


def test():
    with open("./downtown-east2.json") as f:
        lines = f.readlines()

    in_data = lines[:10]
    Sensors(Sensors.insert_data, in_data)

    data = []

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
