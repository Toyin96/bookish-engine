counter = 0
overall_average = 0

gallons = int(input("Enter the gallons used (-1 to end):"))
miles = int(input("Enter the miles driven:"))

while gallons != -1:
    milespergallon = miles / gallons
    print(f'The miles/gallon for this tank was {milespergallon:.2f}')
    counter += 1
    overall_average += milespergallon
    gallons = int(input("Enter the gallons used (-1 to end):"))
    miles = int(input("Enter the miles driven:"))
    
    
    
print(f'The overall average miles/gallon was {overall_average:.2f}')