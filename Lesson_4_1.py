# 1. Создать 3 переменные с одинаковыми данными (и одинаковым типом) и с одинаковыми идентификаторами (не присваивая значения переменных друг другу)
# 2. Создать 2 переменные с одинаковыми данными (и одинаковым типом) и с разными идентификаторами
# 3. Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы, но при этом остались одинаковые данные (и одинаковым типом),
#    а у 2-х последних стали одинаковые идентификаторы и остались одинаковые данные. #
# Try 2 #

bull = (2, 4, 12,)
circle = (2, 4, 12,)
kole = (2, 4, 12,)
print(bull==circle)
print(bull==kole)
print(kole==circle)
print(id(bull))
print(id(circle))
print(id(kole))
print("-" * 50)

case = [23, 42, "we"]
lori = [23, 42, "we"]
print(case == lori)
print(case is lori)
print("-" * 50)


print(list(bull) == list(circle))
print(list(bull) == list(kole))
print(list(kole) == list(circle))
print(id(list(bull)))
print(id(list(circle)))
print(id(list(kole)))
print("-" * 50)

case = tuple(case)
lori = tuple(lori)
print(tuple(case) == tuple(lori))
print(tuple(case) is tuple(lori))
print("-" * 50)