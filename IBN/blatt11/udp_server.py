import socket

host = 'localhost'
port = 5555
buffer_size = 20

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

while True:
	data, addr = s.recvfrom(buffer_size)
