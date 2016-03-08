# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Runner for FileReader, DBConnect and QueryDB

import MySQLdb
import time
from FileReader import FileReader
from DBConnect import DBConnect
from DataParser import DataParser
from QueryDB import QueryDB

class Runner:
	#Constructor getting the file url
	def __init__(self, url):
		self.url = url
	
	#Start reading data end send to db
	#in a set interval
	def run(self):
		#Connect to db, receive db connection Object
		dbConnect = DBConnect()
		dbConnect.connect()
		db = dbConnect.getConnection()
	
		#Start reading the file, receive results list with data
		fileReader = FileReader(self.url)
		fileReader.open_and_read_file()
		result = fileReader.getResults()
		
		#Parse the result data to appropriate format
		dataParser = DataParser()
		sortedResults = dataParser.sortData(result)
		
		#Send data to database
		queryDB = QueryDB(db)
		queryDB.query(sortedResults)
		
		#Close connection to database

		dbConnect.disconnect()
if __name__ == '__main__':
	"""
	This is the main method and is executed when you type "Python Runner.py"
	in your terminal.
	"""
	Runner = Runner("../data/test.json")
	Runner.run()