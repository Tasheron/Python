# Найти корни квадратного уравнения Ax² + Bx + C = 0

import math

a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
D = b**2 - 4 * a * c
if D < 0:
    print("Корней нет")
elif D == 0:
    x = -b / 2 * a
    print(x)
else:
    x1 = int((-b + math.sqrt(D)) / 2 * a)
    x2 = int((-b - math.sqrt(D)) / 2 * a)
    print(x1, x2)