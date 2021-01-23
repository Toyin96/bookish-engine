a = 0
p = 1000.00
r = 0.07
n = 10

for number in range(1, 11):
    a = p * (1 + r)**number
    print(f'year {number}: {a:10.2f}')