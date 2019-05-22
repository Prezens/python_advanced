import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 8888))
sock.listen(5)

# Указывает на то, что пакеты будут широковещательные
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# Позволяет нескольким приложениям "слушать" (резервировать порт) сокет
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client, addr = sock.accept()
result = client.recv(1024)
client.close()

print('Message: ', result.decode('utf-8'))
