#SLIIT Assignment 1 - Task 1 - Server     ( Lakmal Karunarathna )

import socket
IP = '127.0.0.1' #loopback
PORT = 1050      #non-privileged ports >1023
AMT_DATA = 1024 

#Create the socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket with proper IP and a PORT  bind()

serverSocket.bind((IP,PORT))

#Configure no.of clients can listen simultaneously

serverSocket.listen(2)

count = 0
s = ''

#Accept client connections

while(True):

    (clientConnected, clientAddress) = serverSocket.accept()

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))

    if count == 0:
        dataFromClient = clientConnected.recv(AMT_DATA)
        temp_str = dataFromClient.decode()

        #set the client1 send data

        s = temp_str[0]
        clientConnected.close()

    else :
        #Increment of Char

        s = chr(ord(s) + 1)

        #Send data back to the client

        clientConnected.send(s.encode())
        clientConnected.close()
        break

    count += 1