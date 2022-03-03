from cmath import sqrt


list = []

for i in range(0, 3):
    list.append(int(input(f"Введите число {i+1}: ")))

if list[0] == list[1] == list[2]:
    print(f"Все числа ранвы {list[0]}")
if list[2] < list[0] > list[1]:
    print(f"Наибольшее число: {list[0]}")
elif list[1] > list[2]:
    print(f"Наибольшее число: {list[1]}")
else:
    print(f"Наибольшее число: {list[2]}")