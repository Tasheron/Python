n = int(input("введите N: "))
if n < 2:
    print("n не входит в возможный диапазон")
else:
    if n % 2 == 0:
        for i in range(2, n + 1):
            print("")