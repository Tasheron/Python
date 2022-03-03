# Возведите число А в натуральную степень B используя цикл

A = int(input("Введите A: "))
B = int(input("Введите B: "))
temp = A
for i in range(1, B):
    A *= temp
print("Результат вовзедения A в " + str(B) + " степень равен " + str(A))