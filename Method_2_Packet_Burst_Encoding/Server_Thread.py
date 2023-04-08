import socket
import Sniffer

# create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set the IP address and port number of the server
server_address = ('0.0.0.0', 1234)

# bind the socket to the server address and port
server_socket.bind(server_address)
print("d1")

# listen for incoming connections
server_socket.listen(1)

print('Waiting for a connection...')

while True:
	#Use threading for multtiple files
	client_socket, client_address = server_socket.accept()
	print('Connection from ', client_address, ' established.')
	print(client_address[0])
	Sniffer.capture_tcp_packets(client_address[0], 1234)
	break
