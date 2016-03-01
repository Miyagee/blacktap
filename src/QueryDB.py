# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Send data from result to database

import MySQLdb;

class QueryDB:
	def __init__(self, result):
		self.result = result
		self.db = connect()
		
	def connect(self):
		db = MySQLdb.connect(host = ip,
							 user = username
							 passwd = password
							 db = db_name)
		return db
	
	def query(self):
		cursor = self.db.cursor()
		for values in result:
			if values[0] == "torque_at_transmission":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "torque_at_transmission":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "engine_speed":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "vehicle_speed":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "accelerator_pedal_position":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "parking_brake_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "brake_pedal_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "transmission_gear_position":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "gear_lever_position":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "odometer":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "ignition_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "fuel_level":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "fuel_consumed_since_restart":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "door_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "headlamp_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "high_beam_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "windshield_wiper_status":
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "latitude":	
				cursor.execute("INSERT INTO",values[0],values[1])
			else if values[0] == "longitude":
				cursor.execute("INSERT INTO",values[0],values[1])