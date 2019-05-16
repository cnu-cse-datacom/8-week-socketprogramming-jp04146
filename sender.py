#!/usr/bin/env python3
import socket
import sys
import os

FLAGS = None
class ClientSocket():

	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	def socket_send(self):
		
		sentMessage = "file recv from "+FLAGS.ip
		self.socket.sendto(sentMessage.encode(), (FLAGS.ip, FLAGS.port)) 
		
		fileName = input("input your file name : ")
		print("Is there? : ", os.path.isfile(fileName))
		self.socket.sendto(fileName.encode(), (FLAGS.ip, FLAGS.port))

		fileSize = os.path.getsize(fileName)
		self.socket.sendto(str(fileSize).encode(), (FLAGS.ip, FLAGS.port))

		startMessage, _ = self.socket.recvfrom(2000)
		print(startMessage.decode())
		currentSize = 0
		with open(fileName, 'rb') as f:

			count = 1

			while True:
                                data = f.read(1024)
                                print(type(data))

                                self.socket.sendto(data, (FLAGS.ip, FLAGS.port))

                                currentSize += len(data)
                                #currentSize = 1024*count
                                if currentSize > fileSize:
	                                currentSize = fileSize
 

                                count = count+1
                                print("current_size / total_size = %d/%d, %f%%" %(currentSize, fileSize, 100*currentSize/fileSize))
                                if currentSize >= fileSize:
                                        break
			
		self.socket.close()
		print("socket closed")

	def main(self):
		self.socket_send()
	
if __name__ == '__main__':

	import argparse
	
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--ip', type=str, default='127.0.0.1')
	parser.add_argument('-p', '--port', type=int, default=8000)

	FLAGS, _ = parser.parse_known_args()

	client_socket = ClientSocket()
	client_socket.main()
