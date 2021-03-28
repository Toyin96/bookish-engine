import json


def get_new_username():
    """Greets user"""
    username = []
    username = input("welcome user! kindly enter your name: ")
    filename = 'new_user.json'
    with open(filename, 'w') as fileobject:
        json.dump(username, fileobject)
    return username


def welcome_user():
    """Welcomes an existing user if available, or stores the new user in the file"""
    username = stored_username()
    if username:
        answer = input(f"is '{username}' your correct username? \nEnter Yes OR No: ")
        if answer.lower().strip() == 'yes':
            print(f"Welcome {username}!")
        elif answer.lower().strip() == 'no':
            username = get_new_username()
            print(f"We'll remember you when you come back {username}!")
        else:
            print("You entered the wrong input dimmadumbass!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back {username}!")


def stored_username():
    try:
        filename = 'new_user.json'
        with open(filename) as f:
            result = json.load(f)
            if result:
                return result
    except FileNotFoundError:
        get_new_username()


welcome_user()
