p = 1000.00
r = 0.07
n = 30

a = p * (1 + r)**n
print('year  Investment Return')
for number in range(1,31):
    print(f'{number} {1000 * (1 + 0.07)**number:>13.2f}')