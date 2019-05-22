import os
import socket

unix_sock_name = 'unix.sock'  # Имя сокет файла
# AF_UNIX - Unix-socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock_name):
    os.remove(unix_sock_name)

# Т.к. передан AF_UNIX, то мы не получаем исключения и передаем имя файла
# В качестве точки обмена будет выступать файл
sock.bind(unix_sock_name)

while True:
    try:
        result = sock.recv(1024)
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message: ', result.decode('utf-8'))
