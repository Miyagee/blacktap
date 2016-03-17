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
	
	#Finding the last trip id in database data table
	def find_trip_id(self):
		self.cursor.execute("SELECT MAX(tripId) FROM `skyclouds_blacktap`.`data`")
		#self.trip_id = self.cursor.fetchone()
                #self.trip_id += 1
                self.trip_id = 1
	
	#Loop the result list, send query according to result name
	def query(self, sortedResults):
		timestamp = datetime.datetime.fromtimestamp(int(sortedResults[0])).strftime('%Y-%m-%d %H:%M:%S')
		
		#Updating trip id
		self.find_trip_id()
		
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
			if index != 20:
				query = query + ","
		query = query + ");"
		print query
		self.cursor.execute(query)