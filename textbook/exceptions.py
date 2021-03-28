try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide a number by Zero...you dumbtard!")

print("So what is your name again you dimmadumbass")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    try:
        first_number = input("\nFirst number: ")
        if first_number.lower().strip() == 'q':
            break
        second_number = input("Second number: ")
        if second_number.lower().strip() == 'q':
            break
        try:
            answer = int(first_number) / int(second_number)
            print(answer)
        except ZeroDivisionError:
            print('You cannot divide a number by 0')
    except ValueError:
        print("You entered a string instead of an integer")


filename = 'C:/Users/ADMIN/Downloads/text files/pi_digits.txt'
total = []

with open(filename) as fileobject:
    content = fileobject.read()
for i in content:
    total += i.split(" ")
print(f"There are about {len(total)} in the document '{filename}'")
