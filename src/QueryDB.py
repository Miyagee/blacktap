# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Send data from result to database

import MySQLdb
import datetime

class QueryDB:
	#Constructor, getting the db connection
	def __init__(self, db):
		self.cursor = db.cursor()
	
	#Loop the result list, send query according to result name
	def query(self, sortedResults):
		timestamp = datetime.datetime.fromtimestamp(int(sortedResults[0])).strftime('%Y-%m-%d %H:%M:%S')
		
		query = ("INSERT INTO `skyclouds_blacktap`.`data` (" +\
														"`bil_idBil`," +\
														"`timestamp`," +\
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
		query = query + "'" + timestamp + "',"
		
		for index in range(1,len(sortedResults)):
			if len(sortedResults[index]) > 0:
				query = query + "'" +str(sum(sortedResults[index])/float(len(sortedResults[index]))) + "'"
			else:
				query = query + "'"+ "0" + "'"
			if index != 19: 
				query = query + ","
		query = query + ");"
		print query
		self.cursor.execute(query)