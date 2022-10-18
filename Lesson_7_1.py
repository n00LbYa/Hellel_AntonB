# Сделать программу в виде функций в которой нужно будет угадывать число.


secret = input("Введите число от 1 до 15: ")
if not secret.isdigit() or int(secret) <= 0:
    print("Вы ввели не коректное число! Попробуйте еще раз")
target = int(secret)
find_secret = []
for i in range(1, 15):
    find_secret.append(i)
answer = 0
while answer < len(find_secret):
    if find_secret[answer] == target:
        print("Ваше число:", int(find_secret[answer]))
        break
    answer += 1



