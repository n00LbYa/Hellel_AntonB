# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n). Исключения составляют все числа кратные цифре 3.
# Реализовать в 2-х вариантах: используя цикл while и цикл for

n = input("Введите чисто 'n': ")
b = 0

for t in range(1, int(n)+1):
      if t % 3 == 0:
          continue
      b += t ** 3

print(b)


x = 1
sum = 0
while x <= int(n):

    sum = sum + (x * x * x)
    x = x + 1
    if x % 3 == 0:
        continue

print(sum)





