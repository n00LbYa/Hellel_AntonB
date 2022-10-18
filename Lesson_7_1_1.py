import random
secret = int(input("Введите число от 1 до 77: "))

first_item = 1
second_item = 77
guess = random.randint(first_item, second_item)


if secret == guess:
    print('С первого раза!')
else:
    while guess != secret:
        if secret > guess:
            first_item = guess
            guess = random.randint(first_item, second_item)
        elif secret < guess:
            second_item = guess
            guess = random.randint(first_item, second_item)

    print('Вот ваше число', secret)