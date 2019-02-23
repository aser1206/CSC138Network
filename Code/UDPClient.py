from socket import *
serverName = '127.0.0.1'
serverPort = 12544
clientSocket = socket(AF_INET, SOCK_DGRAM)
sentence = raw_input ('Enter a sentence all lowercase: \n')
clientSocket.sendto(sentence.encode(),(serverName,serverPort))
modifiedSentence,serverAddress = clientSocket.recvfrom(1024)
print 'From server: ', modifiedSentence.decode()
clientSocket.close()
