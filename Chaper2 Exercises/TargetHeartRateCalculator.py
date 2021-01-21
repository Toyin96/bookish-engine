age = int(input('Enter your age in years: '))

maximumHeartRate = 220 - age

targetHeartRate = 50/100 * maximumHeartRate
targetHeartRate1 = 85/100 * maximumHeartRate

print('Your maximumHeartRate is', maximumHeartRate, 'while your targetHeartRate rage from', targetHeartRate, '-', targetHeartRate1, 'percent')