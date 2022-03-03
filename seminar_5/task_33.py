# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = randint(0, 5)
coefList = []
string = ""
for i in range(0, k + 1):
    coefList.append(randint(0, 5))
for i in range(k, -1, -1):
    if coefList[i] != 0:
        if coefList == 1:
            if i > 1:
                string += f"x^{i} "
            elif i == 1:
                string += "x "
        else:
            if i > 1:
                string += f"{coefList[i]}*x^{i} "
            elif i == 1:
                string += f"{coefList[i]}*x "
            else:
                string += f"{coefList[i]} "
        if i == 0:
            if len(string) > 2:
                string += "= 0"
            else:
                string += "!= 0"
        else:
            string += "+ "
print(string)
with open('task_33-text.txt', 'w', encoding='utf-8') as text:
    text.write(string)