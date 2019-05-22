import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
sock.send(b'Test')

result = sock.recv(64)
print('Response: ', result)

sock.close()
