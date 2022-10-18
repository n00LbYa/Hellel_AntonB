# Написать программу которая получит имя и возраст пользователя, проверяет возраст и выдаёт
# приветственное сообщение в зависимости от возраста:
# - меньше нуля или ноль или не число: “Ошибка, повторите ввод”;
# - больше нуля до 10 не включая: “Привет, шкет #Имя#”;
# - от 10 до 18 включая: “Как жизнь #Имя#?”
# - больше 18 и меньше 100: “Что желаете #Имя#?”
# - в противном случае: “#Имя#, вы лжете - в наше время столько не живут...”
# Программу необходимо завернуть в вечный цикл.
# После очередной отработки кода, спрашивать у пользователя "Желаете выйти? (Д/Y)".
# Если ответ будет буква "Д" или буква "Y" в любом регистре, то произвести выход из вечного цикла.
# В противном случае продолжить выполнение программы заново.

while True:
   your_name = input("Enter your name: ")
   your_age = input("Enter your age: ")

   if not your_age.isdigit() or int(your_age) <= 0:
        print("Ошибка, повторите ввод")

        answer = input("Хотите выйти? (Д/Y)")
        if answer.upper() in ("Y", "Д"):
            break

   elif int(your_age) < 10:
        print("Привет, шкет {name}".format(name=your_name))

        answer = input("Хотите выйти? (Д/Y)")
        if answer.upper() in ("Y", "Д"):
            break

   elif int(your_age) <= 18:
        print("Как жизнь {name}?".format(name=your_name))

        answer = input("Хотите выйти? (Д/Y)")
        if answer.upper() in ("Y", "Д"):
            break

   elif int(your_age) < 100:
        print("Что желаете {name}?".format(name=your_name))

        answer = input("Хотите выйти? (Д/Y)")
        if answer.upper() in ("Y", "Д"):
            break

   else:
        print("Вы лжете - в наше время столько не живут...")

        answer = input("Хотите выйти? (Д/Y)")
        if answer.upper() in ("Y", "Д"):
            break





