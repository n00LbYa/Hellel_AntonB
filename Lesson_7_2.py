# Дан словарь, создать новый словарь при помощи конструкции генератор словаря, поменяв местами ключ и значение.

dictionary_1 = {76: 25, 23423: 29, -4123: 22, 0: 25, 5432: 31}

dictionary_2 = {value: key for key, value in dictionary_1.items()}

print(dictionary_2)
