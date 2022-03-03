# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
# Т.е. для k = 8, список будет выглядеть так: [-21, 13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

k = int(input("Введите число: "))
list = [0]
temp1 = 1
for i in range(k):
    temp2 = list[i]
    list.append(temp1 + temp2)
    temp1 = temp2
flag = 1
tempList = []
for i in range(1, k + 1):
    tempList.insert(0, list[i] * flag)
    flag *= -1
list = tempList + list
print(list)