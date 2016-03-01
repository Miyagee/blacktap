# Written By: Christoffer A. Nilsen
# Date: 23/02/2016
# Purpose: Read in data from blackbox/file

import json
import time

class FileReader:
	
	#Constructor
	def __init__(self, url):
		self.url = url
		self.first = True
		self.results = []
	
	#Simulate time delay between input	
	def sleeper(self, cur_timestamp, old_timestamp):
		if not self.first:
			if cur_timestamp > old_timestamp:
				time.sleep(cur_timestamp-old_timestamp)
		else:
			self.first = not self.first
			old_timestamp = cur_timestamp
		return old_timestamp
	
	#Opens and read the file with date input
	def open_and_read_file(self):
		
		data = []
		json_data = []
		old_timestamp = 0
		
		with open(self.url) as f:
			data.extend(f.readlines())
			f.close()
		for i in range(len(data)):
			json_data = json.loads(data[i])
			old_timestamp = self.sleeper(json_data["timestamp"], old_timestamp)

			self.results.append([json_data["name"], json_data["value"], json_data["timestamp"]])
			
		print "--::READ DONE::--"
		
	#Getter to get all results
	def getResults(self):
		return self.results