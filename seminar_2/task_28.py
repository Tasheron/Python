# Подсчитать сумму цифр в числе

num = input("Введите число: ")
rez = 0
for i in range(len(num)):
    rez += int(num[i])
print(rez)