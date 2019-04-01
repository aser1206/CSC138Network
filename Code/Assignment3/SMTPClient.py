from socket import *

heloCommand = 'HELO Alice\r\n'

mailserver = '127.0.0.1'
#creating an INET streaming socket
clientSocket = socket(AF_INET, SOCK_STREAM)
#connecting to the mail server on port 25
clientSocket.connect((mailserver, 25))
recvconnect = clientSocket.recv(1024)
print recvconnect

if recvconnect[:3] != '220':
	print '220 reply not received from server.'

#Send HELO command and print server response
#print "Sending First HELO"
clientSocket.send(heloCommand)
recvhelo = clientSocket.recv(1024)
print recvhelo
if recvhelo[:3] != '250':
	print '250 reply not received from server.'

#Send MAIL FROM command and print server response.
#print "Sending MAIL FROM Command"
clientSocket.send("MAIL from: <potus@whitehouse.gov>\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

#Send RCPT TO command and print server response.
#I send the email to myself
#print "Sending RCPT TO Command"
clientSocket.send("RCPT TO: <aser1206@gmail.com>\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

#Send DATA command and print server response.
#print "Sending DATA Command"
clientSocket.send("DATA\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '354':
	print '250 reply not received from server.'


#Send Data and print server response.
# print "Sending Data"
clientSocket.send("\r\n SMTP Mail Client Test\nThank you for your support in California. Together we can make California better\r\n.\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'

#Send QUIT and print server response.
# print "Sending QUIT"
clientSocket.send("QUIT\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '221':
	print '221 reply not received from server.'

print "Mail Sent"
