import socket
import time

host = 'localhost'
port = 5555
buffer_size = 20
message = 'zdr kp'

start = time.time()

for _ in range(1000):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(str.encode(message), (host, port))

print(time.time() - start)
