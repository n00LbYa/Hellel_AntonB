# Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
# Декодировать её в строковый вид в кодировке по умолчанию.
# Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
# И на конец результат снова декодировать в строку.
# (результаты всех преобразований выводить на экран).

our_line = b'r\xc3\xa9sum\xc3\xa9'

our_line = our_line.decode()
print(our_line)

our_line = our_line.encode('Latin1')
print(our_line)

our_line = our_line.decode('Latin1')
print(our_line)