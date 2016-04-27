# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

import time


class DataParser():
    # Empty contructor

    def __init__(self):
        self.first_timestamp = None
        self.first_time = None

    def parseToDict(self, list_of_dicts):
        """This method takes a list of dictionaries and merges it into one."""
        result = {}
        for d in list_of_dicts:
            result[d.get('name')] = d.get('value')
        #result['timestamp'] = list_of_dicts[-1].get('timestamp')

        if self.first_timestamp is None:
            self.first_timestamp = max(e['timestamp'] for e in list_of_dicts)
            self.first_time = time.time()

        result['timestamp'] = self.first_timestamp + \
            int(time.time() - self.first_time)
        return result
