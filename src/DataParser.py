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
		self.timestamp = result[len(result)-1]["timestamp"]
		
		for values in result:
			if values["name"] == "torque_at_transmission":
				self.torque_at_transmission.append(values["value"])
			elif values["name"] == "engine_speed":
				self.engine_speed.append(values["value"])
			elif values["name"] == "engine_speed":
				self.steering_wheel_angle.append(values["value"])
			elif values["name"] == "vehicle_speed":
				self.vehicle_speed.append(values["value"])
			elif values["name"] == "accelerator_pedal_position":
				self.accelerator_pedal_position.append(values["value"])
			elif values["name"] == "parking_brake_status":
				self.parking_brake_status.append(values["value"])
			elif values["name"] == "brake_pedal_status":
				self.brake_pedal_status.append(values["value"])
			elif values["name"] == "transmission_gear_position":
				self.transmission_gear_position.append(values["value"])
			elif values["name"] == "gear_lever_position":
				self.gear_lever_position.append("'" + values["value"] + "'")
			elif values["name"] == "odometer":
				self.odometer.append(values["value"])
			elif values["name"] == "ignition_status":
				self.ignition_status.append(values["value"])
			elif values["name"] == "fuel_level":
				self.fuel_level.append(values["value"])
			elif values["name"] == "fuel_consumed_since_restart":
				self.fuel_consumed_since_restart.append(values["value"])
			elif values["name"] == "door_status":
				self.door_status.append("'" + values["value"] + "'")
			elif values["name"] == "headlamp_status":
				self.headlamp_status.append(values["value"])
			elif values["name"] == "high_beam_status":
				self.high_beam_status.append(values["value"])
			elif values["name"] == "windshield_wiper_status":
				self.windshield_wiper_status.append(values["value"])
			elif values["name"] == "latitude":	
				self.latitude.append(values["value"])
			elif values["name"] == "longitude":
				self.longitude.append(values["value"])
				
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
