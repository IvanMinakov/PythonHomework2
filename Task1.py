num = float(input("Введите вещественеое число: "))
sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print(sum)
