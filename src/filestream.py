import os
import json
import time
import threading
import socket

class FileStream(threading.Thread):

    def __init__(self, filename, address):
        super(FileStream, self).__init__()
        self.daemon = True

        self._data_file = open(filename, 'r')
        self._socket_address = address

        self._virt_start_time = None
        self._real_start_time = None

        self._server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        if os.path.exists(self._socket_address):  # remove pre-existing socketfile
            os.unlink(self._socket_address)

        self._server.bind(self._socket_address)
        self._server.listen(1)

        self.start()

    def run(self):
        connection, _ = self._server.accept()
        for line in self._data_file:
            next_time = json.loads(line)['timestamp']
            if self._virt_start_time is None:
                self._virt_start_time = next_time
                self._real_start_time = time.time()
            else:
                time.sleep(max(0, self._rel(next_time) - self._now()))

            connection.send(line.encode('utf-8'))

    def _now(self):
        return time.time() - self._real_start_time

    def _rel(self, t):
        return t - self._virt_start_time

if __name__ == '__main__':
    while True:
        try:
            f = FileStream('downtown-east2.json', 'data_stream_sock').join()
        except KeyboardInterrupt:
            break
        except:
            pass
