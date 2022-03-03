# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list = [1, 2, 3, 5, 1, 5, 3, 10]
newList = []
for i in range(0, len(list)):
    if not list[i] in newList:
        newList.append(list[i])
print(newList)