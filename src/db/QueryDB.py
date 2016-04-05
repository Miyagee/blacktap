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
	def query(self, sortedResults):
		timestamp = datetime.datetime.fromtimestamp(int(sortedResults[0])).strftime('%Y-%m-%d %H:%M:%S')
                if self._last_time == timestamp:
                    return
                self._last_time = timestamp
		
		#Updating trip id
		
		query = ("INSERT INTO `skyclouds_blacktap`.`data` (" +\
														"`bil_idBil`," +\
														"`timestamp`," +\
														"`tripId`," +\
														"`steering_wheel_angle`," +\
														"`torque_at_transmission`," +\
														"`engine_speed`," +\
														"`vehicle_speed`," +\
														"`accelerator_pedal_position`," +\
														"`parking_brake_status`," +\
														"`brake_pedal_status`," +\
														"`transmission_gear_position`," +\
														"`gear_lever_position`," +\
														"`headlamp_status`," +\
														"`odometer`," +\
														"`ignition_status`," +\
														"`fuel_level`," +\
														"`fuel_consumed_since_restart`," +\
														"`door_status`," +\
														"`high_beam_status`," +\
														"`windshield_wiper_status`," +\
														"`latitude`," +\
														"`longitude`" +\
														") VALUES (" + "'1',")
		query = query + "'" + timestamp + "'," + str(self.trip_id) + ","
		
		for index in range(1, len(sortedResults)):
			if len(sortedResults[index]) > 0:
				query = query + str(sortedResults[index][0])
			else:
				query = query + "0"
			if index != 19:
				query = query + ","
                        print index
		query = query + ");"
		self.cursor.execute(query)
                self._db.commit()
