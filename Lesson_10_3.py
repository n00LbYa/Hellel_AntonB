# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка: from datetime import datetime
# time = datetime.now()

import datetime


def my_decorator_1(first_function):
    now_time = datetime.datetime.now()
    def wraper():
        print("Время начало выполнения функции", datetime.datetime.now() - now_time)
        first_function()
        print("Конец выполнения функции", datetime.datetime.now() - now_time)

    return wraper

def first_function():
    alone = 2
    not_alone = 4
    together = alone * not_alone
    print(together)


def second_function():
    print("Thanks for your advice!")
    bones = 15
    broke = 3
    healthy_bones = bones - broke
    print("Healthy bones =", healthy_bones)

my_decorator_1(first_function)()

my_decorator_1(second_function)()






