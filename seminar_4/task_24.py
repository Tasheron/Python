# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
min = 100000
max = -100000
for i in range(0, len(list)):
    temp = list[i]-int(list[i])
    if temp != 0:
        if temp > max:
            max = temp
        elif temp < min:
            min = temp
print(round(max - min, 5))