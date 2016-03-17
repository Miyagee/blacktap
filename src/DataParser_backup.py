# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

class DataParser():
	#Empty contructor
	def __inif__(self):
		pass
		
	#Sort data into lists and return one multidimentional list
	def sortData(self, result):
		self.steering_wheel_angle = []
		self.torque_at_transmission = []
		self.engine_speed = []
		self.vehicle_speed = []
		self.accelerator_pedal_position = []
		self.parking_brake_status = []
		self.brake_pedal_status = []
		self.transmission_gear_position = []
		self.gear_lever_position = []
		self.odometer = []
		self.ignition_status = []
		self.fuel_level = []
		self.fuel_consumed_since_restart = []
		self.door_status = []
		self.headlamp_status = []
		self.high_beam_status = []
		self.windshield_wiper_status = []
		self.latitude = []
		self.longitude = []
		self.timestamp = result[len(result)-1][2]
		
		for values in result:
			if values[0] == "torque_at_transmission":
				self.torque_at_transmission.append(values[1])
			elif values[0] == "engine_speed":
				self.engine_speed.append(values[1])
			elif values[0] == "engine_speed":
				self.steering_wheel_angle.append(values[1])
			elif values[0] == "vehicle_speed":
				self.vehicle_speed.append(values[1])
			elif values[0] == "accelerator_pedal_position":
				self.accelerator_pedal_position.append(values[1])
			elif values[0] == "parking_brake_status":
				self.parking_brake_status.append(values[1])
			elif values[0] == "brake_pedal_status":
				self.brake_pedal_status.append(values[1])
			elif values[0] == "transmission_gear_position":
				self.transmission_gear_position.append(values[1])
			elif values[0] == "gear_lever_position":
				self.gear_lever_position.append(values[1])
			elif values[0] == "odometer":
				self.odometer.append(values[1])
			elif values[0] == "ignition_status":
				self.ignition_status.append(values[1])
			elif values[0] == "fuel_level":
				self.fuel_level.append(values[1])
			elif values[0] == "fuel_consumed_since_restart":
				self.fuel_consumed_since_restart.append(values[1])
			elif values[0] == "door_status":
				self.door_status.append(values[1])
			elif values[0] == "headlamp_status":
				self.headlamp_status.append(values[1])
			elif values[0] == "high_beam_status":
				self.high_beam_status.append(values[1])
			elif values[0] == "windshield_wiper_status":
				self.windshield_wiper_status.append(values[1])
			elif values[0] == "latitude":	
				self.latitude.append(values[1])
			elif values[0] == "longitude":
				self.longitude.append(values[1])
				
		self.sortedResults = [
					self.timestamp,
					self.steering_wheel_angle,
					self.torque_at_transmission,
					self.engine_speed,
					self.vehicle_speed,
					self.accelerator_pedal_position,
					self.parking_brake_status,
					self.brake_pedal_status,
					self.transmission_gear_position,
					self.gear_lever_position,
					self.headlamp_status,
					self.odometer,
					self.ignition_status,
					self.fuel_level,
					self.fuel_consumed_since_restart,
					self.door_status,
					self.high_beam_status,
					self.windshield_wiper_status,
					self.latitude,
					self.longitude
		]
		return self.sortedResults
