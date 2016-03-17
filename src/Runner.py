# Written By: Christoffer A. Nilsen
# Date: 03/01/2016
# Purpose: Runner for DBConnect, QueryDB, UNIXReader and DataParser

import MySQLdb
import time
import thread
import socket
import json

from FileReader import FileReader
from DBConnect import DBConnect
from DataParser import DataParser
from UNIXReader import UNIXReader
from QueryDB import QueryDB

class Runner(object):
	#Constructor getting the file url
	def __init__(self):
		self.results = []
	
	#Start reading data end send to db
	#in a set interval
	def run(self):
		#Connect to db, receive db connection Object
		db_connect = DBConnect()
		db_connect.connect()
		db = db_connect.get_connection()
		
		"""
		#Start reading the file, receive results list with data
		fileReader = FileReader(self.url)
		fileReader.open_and_read_file()
		result = fileReader.getResults()
		"""
		
		#Setting up a class object and connecting.
		unix_reader = UNIXReader("upload_stream.sock")
		unix_reader.connect()
		
		#Data parser class object to parse receieved data
		data_parser = DataParser()
		
		#Query class object getting ready to query database
		query_db = QueryDB(db)

		while True:
			
			#Receive data from unix reader object
			data = unix_reader.revc_socket()

			json_data = json.loads(data)
            print "Receiver: json_data"
			
			#Parse the result data to appropriate format
			sorted_results = dataParser.sortData(json_data)
			
			for value in sorted_results:
				print value
				
			'''
			if dbConnect.check_connection():
				#Send data to database
				query_db.query(sorted_results)
			else: 
				dbConnect.connect()
				#Send data to database
				query_db.query(sorted_results)
			'''
		#Close connection to database
		db_connect.disconnect()

if __name__ == '__main__':
	"""
	This is the main method and is executed when you type "Python Runner.py"
	in your terminal.
	"""
	runner = Runner()
	runner.run()
