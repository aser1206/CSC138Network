from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#prepare a sever socket
serverPort = 5333
serverSocket.bind(("", serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

while True:

	#Establish the connection
	print 'Server running and ready to recieve...'
	connectionSocket, addr = serverSocket.accept()

	try:
		message =  connectionSocket.recv(1024)

		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		# Send one HTTP header line into the socket
		#http://127.0.0.1:5333/HelloWorld.html
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n")

		# Send the content of the requested file to the connection socket
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i])
		connectionSocket.send("\r\n")

		connectionSocket.close()

	except IOError:
		# Send HTTP response message for file not found
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")

		connectionSocket.send("<h1>404 Not Found</h1>\r\n")
		# Close the client socket
		connectionSocket.close()

serverSocket.close()
sys.exit()
