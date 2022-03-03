# Найти сумму чисел списка стоящих на нечетной позиции

list = [1, 2, 3, 4, 5, 6, 7]
sum = 0
for i in range(0, len(list), 2):
    sum += list[i]
print(sum)