print("Welcome to toyin's master calculator \n")
while True:
    input1 = input("Enter first number or enter 'q' to end: ")
    if input1.lower().strip() == 'q':
        break
    input2 = input("Enter first number or enter 'q' to end: ")
    if input2.lower().strip() == 'q':
        break

    try:
        result = int(input1) + int(input2)
        print(f"Th result is: {result}")
    except ValueError:
        print("Kindly enter a number sir/ma and not a text")


alice = 'alice.txt'
content = ''
alice_list = []

try:
    with open(alice, 'r+') as fileobject:
        for i in fileobject.read().strip():
            content += i
        alice_list = content.split(" ")

except FileNotFoundError:
    pass

print(len(alice_list))
print(alice_list)

my_message = 'Is this truly working'
filename = 'names.txt'
with open(filename, 'w') as fileobject:
    fileobject.write(my_message)


