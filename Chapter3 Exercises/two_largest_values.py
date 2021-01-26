#(Nested Control Statements) Use a loop to find the two largest values of 10 numbers entered

largest = 0
second_largest = 0


for num in range(10):
    temp = int(input('Enter an integer: '))
    
    if temp > largest:
        second_largest = largest
        largest = temp
        
    if temp < largest and temp > second_largest:
        second_largest = temp
        
        
print(f'largest number is {largest} while second_largest is {second_largest}')        