# Написать программу, которая состоит из вечного цикла ожидающего ввод числа
# или одно из значений: "выход", "exit", "quit", "e" или "q" в любом регистре.
# При вводе одного из этих значений происходит выход из вечного цикла.
# При любом другом вводе вызывается отдельная функция которая умеет распознавать
# введённые числа. Сама функция ничего не распечатывает, она возвращает строку,
# типа: "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное
# число: Erdf". Затем в цикле выводится это сообщение и цикл начинается заново
# ожидая следующего ввода. Функция на вход принимает строку из ввода из вечного
# цикла. Анализирует её исключительно методом .isdigit() и другими методами
# строк, без доп.библиотек и переводит строку в число, если это возможно.
# Функция умеет распознавать отрицательные числа и десятичные дроби, а так же
# распознаёт десятичные дроби как с точкой, так и с запятой.
# Функция возвращает строку в которой описывается какое число введено -
# отрицательное или положительно, целое или дробное и выводит его или же
# сообщает, что введено не корректное число.
# *Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля
#
# Примеры:
# -6,7 → Вы ввели отрицательное дробное число: -6.7
# 5 → Вы ввели положительное целое число: 5
# 5.4r → Вы ввели не корректное число: 5.4r
# -.777 → Вы ввели отрицательное дробное число: -0.77

def str_to_num(num):
    result = f'вы ввели неверное число {num}'
    num = num[1:] if num.startswith('+') else num

    if num.isdigit():
        if int(num) > 0:
            result = f'вы ввели положительное целое число {int(num)}'
        else:
            result = f'вы ввели ноль'

    elif num[0] == '-' and len(num) > 1 and num[1:].isdigit():
        result = f'вы ввели отрицательное целое число {int(num)}'

    elif num.replace('.', '', 1).replace('-', '', 1).isdigit()\
            and num.find('-') in (-1, 0):
        if float(num) > 0:
            result = f'вы ввели положительное дробное число {float(num)}'
        elif float(num) < 0:
            result = f'вы ввели отрицательное дробное число {float(num)}'

    return result


while True:
    print('Чтобы выйти из программы введите: выход, exit, quit, e, q или в')
    input_str = input('введите число: ').replace(',', '.')
    if input_str.lower() in ('выход', 'exit', 'quit', 'e', 'q', 'в'):
        break
    elif input_str:
        print(str_to_num(input_str))
    else:
        print('Вы ничего не ввели, попробуйте ещё раз')