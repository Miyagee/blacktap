# Written By: Christoffer A. Nilsen
# Date: 15/03/2016
# Purpose: Get data socket from Main server program

import socket
import os

class UNIXReader(object):
	
	#Empty constructor
	def __init__(self, server_adress):
		self.server_adress = server_adress
	
	#Creating and setting up socket and connection
	def connect(self):
		self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		
		if os.path.exists(self.server_adress):
			os.unlink(self.server_adress)
		self.sock.bind(self.server_adress)
		self.connection, self.client_address = sock.accept()
	
	#Receive socket from connection
	def revc_socket(self):	
		self.data = self.connection.recv(250000).decode("utf-8")
		return self.data