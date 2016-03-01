# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Connect to database

import MySQLdb

class DBConnect:
	# Empty constructor
	def __init__(self):
		#empty
	
	#Connect to database
	def connect(self):
		self.db = MySQLdb.connect(host = ip,
							 user = username
							 passwd = password
							 db = db_name)
	
	#Disconnect from Database
	def disconnect(self):
		self.db.close()
	
	#Get the database connection object
	def getConnection(self):
		return self.db