import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8888))
# sock.listen(5)
sock.settimeout(5)  # Сервер будет ожидать 5 секунд
# sock.settimeout(0) -> sock.blocking(False)
# sock.settimeout(None) -> sock.blocking(True)

try:
    client, addr = sock.accept()
except socket.error:
    print('No connections')
except socket.timeout:
    print('Timed out')
else:
    result = client.recv(1024)
    client.close()
    print('Message: ', result.decode('utf-8'))
