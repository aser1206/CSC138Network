from socket import *
serverPort = 12544
serverSocket = socket(AF_INET,SOCK_DGRAM) #create UDP socket
serverSocket.bind (('', serverPort))
#serverSocket.listen(1) #listen for incoming requests
print 'The server is ready to recieve'

while 1:
    message, clientAddress = serverSocket.recvfrom(2048) #read from udp socket into message
    modiffiedMessage = message.decode().upper()
    serverSocket.sendto(modiffiedMessage.encode(),clientAddress)
