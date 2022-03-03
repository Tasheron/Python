# Реализовать алгоритм перемешивания списка

from random import randint

list = [1, 2, 3, 4, 5]
for i in range(0, len(list)):
    rand = randint(0, len(list) - 1)
    list[i], list[rand] = list[rand], list[i]
print(list)