import calc
import view

dictionary = \
    {
        "+": calc.sum,
        "-": calc.dif,
        "*": calc.mult,
        "/": calc.div,
        "**": calc.pow
    }

oper = input("Введите оператор: ")

rez = round(calc.init(dictionary[oper], view.a, view.b), 10)
if rez - int(rez) == 0:
    rez = int(rez)

print(f"Результат операции равен {rez}")