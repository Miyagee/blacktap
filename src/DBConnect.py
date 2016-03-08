# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Connect to database

import MySQLdb

class DBConnect:
	
	# Empty constructor
	def __init__(self):
		pass
	
	#Connect to database
	def connect(self):
		self.db = MySQLdb.connect(host = "mysql.stud.ntnu.no",
								  user = "skyclouds_admin",
								  passwd = "blacktap",
								  db = "skyclouds_blacktap")
	
	#Get the database connection object
	def getConnection(self):
		return self.db
		
	#Disconnect from Database
	def disconnect(self):
		self.db.close()