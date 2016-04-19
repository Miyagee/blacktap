# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

class DataParser():
    #Empty contructor
    def __inif__(self):
        pass

    def parseToDict(self, list_of_dicts):
        """This method takes a list of dictionaries and merges it into one."""
        result = {}
        for d in list_of_dicts:
            result[d.get('name')] = d.get('value')
            print(d)
        result['timestamp'] = list_of_dicts[-1].get('timestamp')
        print(result)

        return result
