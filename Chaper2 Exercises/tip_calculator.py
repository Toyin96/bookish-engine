tip_percent = random.randrange(15, 21)
user_name = input("Hello...welcome to tip calculator! kindly enter your name to proceed: ")
print("Ok cool!")
bill_amount = (input("How much were you charged? ")).replace("$", "")

tip_amount = float(bill_amount) * tip_percent

print(f"Ok {user_name}. Your ideal tip amount should be ${tip_amount}")