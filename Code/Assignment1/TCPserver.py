from socket import *
serverPort = 12543
serverSocket = socket(AF_INET,SOCK_STREAM) #create the welcoming socket
serverSocket.bind (('', serverPort))
serverSocket.listen(1) #listen for incoming requests
print 'The server is ready to recieve'

while 1:
    connectionSocket, addr = serverSocket.accept() #wait on accept for incoming requests

    sentence = connectionSocket.recv (1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
