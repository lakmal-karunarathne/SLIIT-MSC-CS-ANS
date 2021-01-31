#SLIIT Assignment 1 - Task 3 - Client1    ( Lakmal Karunarathna )

import socket
IP = '127.0.0.1' #loopback
PORT = 1050      #non-privileged ports >1023
AMT_DATA = 1024 

#Create the socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket with proper IP and a port bind()

clientSocket.connect((IP,PORT))

#Send data to the server

data = 2.5
clientSocket.send(str(data).encode())
 
#Print the output

print('Client1 has sent %4.2f to the Server' % (data))