# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Send data from result to database

import MySQLdb
import datetime

class QueryDB:
    #Constructor, getting the db connection
    def __init__(self, db):
        self.cursor = db.cursor()
        self.trip_id = 0
        self._db = db
        self._last_time = None

  #Finding the last trip id in database data table
    def find_trip_id(self):
        self.cursor.execute("SELECT MAX(tripId) FROM `skyclouds_blacktap`.`data`")
        self.trip_id = self.cursor.fetchone()[0]

        if self.trip_id is None:
            self.trip_id = 1
        else:
            self.trip_id += 1
            print self.trip_id

  #Loop the result list, send query according to result name
    def query(self, d):
        timestamp = datetime.datetime.fromtimestamp(int(d.get('timestamp'))).strftime('%Y-%m-%d %H:%M:%S')
        if self._last_time == timestamp:
            return
        d['timestamp'] = timestamp
        print(timestamp)

        #Updating trip id
        query = "INSERT INTO skyclouds_blacktap.data (bil_idBil, tripId, "
        query += ', '.join(d.keys())
        query += ") VALUES ( '2', %s, " % self.trip_id
        query += ', '.join("'%s'" % d[key] for key in d.keys())
        query += ");"
        print(query)

        self.cursor.execute(query)
        self._db.commit()
