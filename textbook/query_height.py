name = input("Welcome guess, kindly enter your name: ")
print(f"Hello {name}")

height = input("How tall are you in inches? ")
height = int(height)

if height >= 48:
    print("You're tall enough to ride")
else:
    print("You'll be able to ride when you're a little bit older")