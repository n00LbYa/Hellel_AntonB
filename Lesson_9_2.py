# Написать лямбда-функцию определяющую чётное/нечётное.
# Функция принимает параметр (число) и если чётное, то выдаёт слово “чётное”, если нет - то “не чётное”.

secret_number = input("Введите любое число: ")

math_rule = lambda secret_number: print("Четное!") if secret_number % 2 == 0 else print("Нечетное!")

print(math_rule(int(secret_number)))