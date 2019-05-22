import socket

# AF_INET - константа означает, что мы будем использовать IP-протокол версии 4
# SOCK_DGRAM - константа означает, что мы используем DATAGRAME протокола UDP (т.е. сам UDP протокол)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # экземпляр класса socket
sock.bind(('127.0.0.1', 8888))  # bind - резирвирование порта на локальной машине
result = sock.recv(1024)  # recv - принятие количество байт в размере 1024 (размер буфера)

print('Message: ', result.decode('utf-8'))

sock.close()
