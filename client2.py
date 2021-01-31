#SLIIT Assignment 1 - Task 1 - Client2    ( Lakmal Karunarathna )

import socket
IP = '127.0.0.1' #loopback
PORT = 1050      #non-privileged ports >1023
AMT_DATA = 1024 

#Create the socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the server

clientSocket.connect((IP,PORT))

# Receive data from server

dataFromServer = clientSocket.recv(AMT_DATA)

# Print the output
print('Client2 has received %s from the Server ' % (dataFromServer.decode()))