# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

import json
import time
from threading import Thread, RLock
from collections import defaultdict as dd


class FileReader(Thread):

    # Constructor
    def __init__(self, url):
        super(FileReader, self).__init__()
        self.daemon = True

        self.url = url
        self.results = dd(list)
        self.lock = RLock()

        self.speed_up = 1.0

        # For creating data subsets for test making:
        self.record = False
        self.record_buffer = []
        self.record_index = 1
        self.filename_prefix = "records/record"
        self.rewind = None
        self.add_line = False
        self.line_indices = []

        self.add_speed_limits = True
        self.dump_speed_limit = False
        self.velocities = []

    def change_speed_by(self, k):
        self.speed_up *= k

    def get_speed(self):
        return self.speed_up

    # Simulate time delay between input
    def sleeper(self, cur_timestamp, old_timestamp):
        if cur_timestamp > old_timestamp:
            time.sleep((cur_timestamp - old_timestamp) / self.speed_up)
        return cur_timestamp

    # Opens and read the file with date input
    def run(self):

        data = []
        old_timestamp = None

        if self.add_speed_limits:
            self.g = open(
                self.url[
                    : self.url.find(".json")] +
                "_speed_lims.json",
                "w")
            self.g_buffer = []

        with open(self.url) as f:
            data.extend(f.readlines())
        i = 0
        while i < (len(data)):
            json_data = json.loads(data[i])

            if self.record:
                self.record_buffer.append(data[i])
            elif not self.record and self.record_buffer:
                filename = self.filename_prefix + str(self.record_index)
                self.record_index += 1
                while os.path.isfile(filename):
                    filename = self.filename_prefix + str(self.record_index)
                    self.record_index += 1

                open(filename, "w").write("".join(self.record_buffer))
                self.record_buffer = []
            elif self.rewind:
                i -= 1
                json_data = json.loads(data[i])
                now = json_data['timestamp']
                while 0 < i and json_data['timestamp'] > now - self.rewind:
                    i -= 1
                    json_data = json.loads(data[i])
                    self.results[json_data['name']].pop()
                old_timestamp = None
                self.rewind = None

            if self.add_line:
                self.line_indices.append((i, self.add_line))
                self.add_line = None

            if old_timestamp is None:  # Initial case
                old_timestamp = json_data["timestamp"]
            old_timestamp = self.sleeper(json_data["timestamp"], old_timestamp)

            if self.add_speed_limits:
                if json_data['name'] == 'vehicle_speed':
                    self.velocities.append(json_data['value'])
                self.g_buffer.append(data[i])

                if self.dump_speed_limit or i == len(data) - 1:
                    self.dump_speed_limit = False

                    self.velocities = [e for e in self.velocities if 15 < e]
                    if self.velocities:
                        timestamp = json.loads(self.g_buffer[0])['timestamp']
                        self.g.write(json.dumps({'name': 'speed_limit', 'value': min(30, round(sorted(
                            self.velocities)[len(self.velocities) // 2] / 10.0) * 10), 'timestamp': timestamp}) + "\n")
                        print("wrote", min(30, round(sorted(self.velocities)[
                              len(self.velocities) // 2] / 10.0) * 10))
                        for line in self.g_buffer:
                            self.g.write(line)

                    self.g_buffer.clear()
                    self.velocities.clear()

            with self.lock:
                self.results[json_data['name']].append(
                    (json_data["value"], json_data["timestamp"]))
            i += 1

    def calculate_speed_limits(self):
        self.dump_speed_limit = True

    # Getter to get all results
    def get_data(self):
        return self.lock, self.results
