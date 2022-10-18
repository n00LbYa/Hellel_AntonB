def first_control():
    return secret > guess
def second_control():
    return secret < guess

import random

secret = int(input("Введите число от 1 до 77: "))

first_item = 1
second_item = 77
guess = random.randint(first_item, second_item)


if secret == guess:
    print('С первого раза!')
else:
    while guess != secret:
        if first_control():
            first_item = guess
            guess = random.randint(first_item, second_item)
        elif second_control():
            second_item = guess
            guess = random.randint(first_item, second_item)

    print('Вот ваше число', secret)