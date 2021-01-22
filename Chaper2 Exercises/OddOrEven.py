# Exercise 2.6
""" Program to check if an integer is odd or even"""

a = int(input('Enter an integer: '))

if a % 2 == 0:
    print(a, 'is an even number')
    
if a % 2 != 0:
    print(a, 'is an odd number')