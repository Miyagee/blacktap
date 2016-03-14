import threading
import json
import socket
from sensors import Sensors

class Receiver(threading.Thread):

    def __init__(self, addr):
        super(Receiver, self).__init__()
        self.daemon = True
        self._receive = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self._socket_address = addr
        self.start()

    def run(self):
        self._receive.connect(self._socket_address)
        while True:
            payload = self._receive.recv(4096 * 4).decode('utf-8')
            for obj in payload.strip().split("\n"):
                obj = json.loads(obj)
                Sensors(Sensors.insert_data, obj).join()

if __name__ == '__main__':
    r = Receiver('data_stream_sock').join()
