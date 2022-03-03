# Подсчитать сумму цифр в вещественном числе.

# num = float(input("Введите число: "))
# sum = 0
# temp = 0
# while num != 0:
#     if num % 10 < 0:
#         temp = num % 10
#         while temp < 0:
#             temp * 10
#         sum += temp
#     else:
#         sum += num % 10
#         num //= 10
# print(sum)

num = input("Введите число: ")
sum = 0
for i in range(0, len(num)):
    if num[i] != ".":
        sum += int(num[i])
print(sum)