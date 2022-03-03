# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму

list = []
num = 1
sum = 0
N = int(input("Введите N: "))
for i in range(1, N + 1):
    num = (1 + 1 / i)**i
    sum += num
    list.append(num)
print(list)
print(sum)