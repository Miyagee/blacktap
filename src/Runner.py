# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Runner for FileReader, DBConnect and QueryDB

import MySQLdb
import time

class Runner:
	#Constructor getting the file url
	def __init__(self, url):
		self url = url
	
	#Start reading data end send to db
	#in a set interval
	def run(self):
		#Connect to db, receive db connection Object
		DBConnect = DBConnect()
		DBConnect.connect()
		db = DBConnect.getConnection()
	
		#Start reading the file, receive results list with data
		FileReader = FileReader(self.url)
		result = FileReader.getResults()
		
		#Send data to database
		QueryDB = QueryDB(db)
		QueryDB.query(result)
		
		#Close connection to database
		DBConnect.disconnect()

		
Runner = Runner("../data/test.json")
Runner.run()