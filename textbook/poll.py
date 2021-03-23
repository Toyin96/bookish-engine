users = {}
session = True
mode = ""

while session:
    mode = input("would you like to partake in this poll? enter 'Yes' or 'No': ")
    if mode.lower() == "no":
        print("\nThank you for stopping by.")
        print(f"\nHere is a list of users that partook in the poll: \n{users}")
        break
    user_name = input("Ok great choice! Kindly enter your name: ")
    user_response = input("Tell us how you're feeling today: ")

    users[user_name] = user_response