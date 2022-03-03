# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

list = []
num = 1
N = int(input("Введите N: "))
for i in range(0, N):
    if i != 0:
        num *= -3
        list.append(num)
    else:
        list.append(num)
print(list)