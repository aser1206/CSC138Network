from socket import *
serverName = '127.0.0.1'
serverPort = 12543
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input ('Enter a sentence all lowercase: \n')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence.decode())
clientSocket.close()
