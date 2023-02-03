num = int(input("Введите целое не отрицательное число: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
    print(f"{factorial},", end=" ")
