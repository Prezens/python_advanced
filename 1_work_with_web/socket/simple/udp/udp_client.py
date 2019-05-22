import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # экземпляр класса socket
sock.sendto(b'Test message', ('127.0.0.1', 8888))  # sendto - отправка байт-строки по адресу
