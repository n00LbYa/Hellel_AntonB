# Используя input() ввести предложение состоящее из двух слов.
# Создать 2 переменные и в каждую записать по 1 введённому слову используя методы строк.
# Создать новую переменную 3-мя разными способами форматирования (фактически 3 переменные),
# которая бы состояла из введённых слов в обратном порядке, первое слово должно состоять только из больших букв,
# а второе с первой заглавной буквы и остальных маленьких.
# В начале предложения должен быть восклицательный знак,а в конце вопросительный.
# Используя только атрибуты функции print() вывести первоначальную строку и получившиеся разными способами
# форматирования через разделитель "<<<>>>", вывод сделать в файл.

sentence = input("Text your sentence:")
first_word = sentence.split()[0]
second_word = sentence.split()[1]
print(first_word)
print(second_word)
third_item_1 = sentence[::-1]
third_item_2 = sentence.split()[0].upper(), sentence.split()[1].capitalize()
third_item_3 = "!" + sentence.__add__('?')
my_file = open("text.txt", "w")
print(sentence, file=my_file, end="<<<>>>")
print(third_item_1, file=my_file, end="<<<>>>")
print(third_item_2, file=my_file, end="<<<>>>")
print(third_item_3, file=my_file, end="<<<>>>")
my_file.close()

