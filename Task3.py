n = int(input())
summ = [round((1+1/i)**i, 2) for i in range(1, n+1)]
print(f'Последовательность: {summ}\nСумма: {round(sum(summ), 2)}')
