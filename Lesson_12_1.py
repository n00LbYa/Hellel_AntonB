# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные (4 функции input()).
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дозаписать оставшиеся 2 строки.
# В итогом файле должны быть 4 строки, каждая из которых должна начинаться с новой строки.

first_line = input("Enter the line: ")
second_line = input("Enter the line: ")
third_line = input("Enter the line: ")
fourth_line = input("Enter the line: ")

our_file = open('exampe.txt', 'w')
our_file.write(first_line)
our_file.write('\n')
our_file.write(second_line)
our_file.close()

with open('exampe.txt', 'a') as our_file:
    our_file.write('\n')
    our_file.write(third_line)
    our_file.write('\n')
    our_file.write(fourth_line)
