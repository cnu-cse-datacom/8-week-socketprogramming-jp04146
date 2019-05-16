#! /usr/bin/env python3
import socket
import sys
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 8000
s.bind(('',port))

SAVE_DIR = './data'

start, addr = s.recvfrom(2000)
print(start.decode())

fileName, addr = s.recvfrom(2000)
print("File Name : ", fileName.decode())

fileSize, addr = s.recvfrom(2000)
print("File Size : ", fileSize)
fileSize=int(fileSize.decode())

s.sendto("File Transmit Start....".encode(), addr)

recv_file = SAVE_DIR+'/'+fileName.decode()
currentSize = 0
with open(os.path.join(SAVE_DIR, fileName.decode()), 'wb') as f:

	print('receiving data...')

	while True:
                data, addr = s.recvfrom(1024)
                print(type(data))
                f.write(data)

                currentSize += len(data)
                #currentSize += 1024
                if currentSize > fileSize:
                        currentSize = fileSize
 
                print("current_size / total_size = %d/%d, %f%%" %(currentSize, fileSize, 100*currentSize/fileSize))
                if currentSize >= fileSize:				
                        break
        

print('Successfully get the file')
s.close()
print('socket closed')

