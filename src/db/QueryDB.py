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
        self._legal_fields = {u'accelerator_pedal_position', 'timestamp', u'transmission_gear_position', u'fuel_level', u'engine_speed', u'fuel_consumed_since_restart', u'longitude', u'odometer',
                u'vehicle_speed', u'brake_pedal_status', u'latitude', u'speed_limit', u'turn_signals',
                u'forgot_signals', u'speeding', u'aggressive', u'gear_suggestion', u'fuel_usage10'}

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

        invalids = [key for key in d if key not in self._lega_fields]
        if invalids:
            raise Exception("KeyNotADatabaseValueError: " + ", ".join(invalids))

        query = "INSERT INTO skyclouds_blacktap.data (bil_idBil, tripId"
        query += ', '.join([""] + list(d.keys()))
        query += ") VALUES ( '2', %s" % self.trip_id
        query += ', '.join([""]+["'%s'" % v for v in d.values()])
        query += ");"

        self._db.commit()
