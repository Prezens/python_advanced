from urllib import request

response = request.urlopen('http://example.com')

print(response.status)
print(response.getcode())
print(response.msg)
print(response.reason)
# Получаем заголовки в виде внутреннего объекта
print(response.headers)
# Получаем словарь всех заголовков
print(response.getheaders())
# Получение заголовка
print(response.headers.get('Content-Type'))
print(response.getheaders('Content-Type'))
