# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Send data from result to database

import MySQLdb

class QueryDB:
	#Constructor, getting the db connection
	def __init__(self, db):
		self.cursor = db.corsor()
	
	#Loop the result list, send query according to result name
	def query(self, result):
		for values in result:
			if values[0] == "torque_at_transmission":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "torque_at_transmission":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "engine_speed":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "vehicle_speed":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "accelerator_pedal_position":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "parking_brake_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "brake_pedal_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "transmission_gear_position":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "gear_lever_position":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "odometer":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "ignition_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "fuel_level":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "fuel_consumed_since_restart":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "door_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "headlamp_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "high_beam_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "windshield_wiper_status":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "latitude":	
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				
			else if values[0] == "longitude":
				self.cursor.execute("INSERT INTO ",values[0]," VALUES (",values[1],");")
				