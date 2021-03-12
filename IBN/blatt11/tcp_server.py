import socket

host = 'localhost'
port = 5555
buffer_size = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

while True:
	conn, addr = s.accept()
	data = conn.recv(buffer_size)

conn.close()
