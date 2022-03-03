# Определить, присутствует ли в заданном списке строк, некоторое число

list = ["asd", "asdfew", "asdasd", "4", "adads"]
flag = False
num = int(input("Введите число: "))
for i in range(0, len(list)):
    if list[i] == str(num):
        flag = True
print(flag)