# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

numbers_list = []
with open('task_35-text.txt') as f:
    lines = f.readlines()
f.close()

numbers_string = lines[0]
numbers_list = []
for num_str in numbers_string.split():
    num_int = int(num_str)
    numbers_list.append(num_int)

print(numbers_list)

for i in range(2,len(numbers_list)):
    if numbers_list[i] -1  == numbers_list[i-1]:
        pass
    else:
        print(numbers_list[i]-1)