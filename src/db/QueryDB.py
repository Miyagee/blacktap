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
        self._legal_fields = {u'accelerator_pedal_position', 'timestamp', u'transmission_gear_position', u'fuel_level', u'engine_speed', u'fuel_consumed_since_restart', u'longitude', u'odometer', u'vehicle_speed', u'brake_pedal_status', u'latitude'}

  #Finding the last trip id in database data table
    def find_trip_id(self):
        self.cursor.execute("SELECT MAX(tripId) FROM `skyclouds_blacktap`.`data`")
        self.trip_id = self.cursor.fetchone()[0]

        if self.trip_id is None:
            self.trip_id = 1
        else:
            self.trip_id += 1

  #Loop the result list, send query according to result name
    def query(self, d):
        timestamp = datetime.datetime.fromtimestamp(int(d.get('timestamp'))).strftime('%Y-%m-%d %H:%M:%S')
        if self._last_time == timestamp:
            return
        d['timestamp'] = timestamp

        #Updating trip id
        self.tmp_set = self.tmp_set | set(d.keys()) if "tmp_set" in dir(self) else set()

        query = "INSERT INTO skyclouds_blacktap.data (bil_idBil, tripId"
        query += ', '.join([""] + [key for key in d if key in self._legal_fields])
        query += ") VALUES ( '2', %s" % self.trip_id
        query += ', '.join([""]+["'%s'" % v for k,v in d.items() if k in self._legal_fields])
        query += ");"

        print query
        self._db.commit()
