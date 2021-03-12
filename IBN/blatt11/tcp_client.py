import socket
import time

host = 'localhost'
port = 5555
buffer_size = 20
message = 'zdr kp'

start = time.time()

for _ in range(1000):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.send(str.encode(message))
	s.close()

print(time.time() - start)
