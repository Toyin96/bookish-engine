num1 = float(input('Enter an integer: '))
num2 = float(input('Enter an integer: '))
num3 = float(input('Enter an integer: '))


small = min(num1, num2, num3)
small3 = max(num1, num2, num3)


if num1 != small and num1 != small3:
      small2 = num1

if num2 != small and num2 != small3:
      small2 = num2

if num3 != small and num3 != small3:
      small2 = num3

print('The numbers in ascending order are', small, small2, small3)