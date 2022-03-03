# Вычислить число pi c заданной точностью d. Пример: при d = 0.001, pi = 3.141

from cmath import pi

d = float(input("Введите d: "))
count = 0
while d != 1:
    d *= 10
    count += 1
print(round(pi, count))