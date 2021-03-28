import json


def collect_favorite_num():
    """Collects user's favorite number"""
    fav_number = int(input("Hello user, what is your favorite number? "))
    if fav_number:
        status = store_fav_number(fav_number)
        if status:
            print("Your favorite number has been stored successfully.")
        else:
            print("For some reason we couldn't store your number")
    else:
        print("You did not enter an integer!")


def store_fav_number(number):
    """Stores the user's favorite number into the database"""
    try:
        filename = 'fav_num.json'
        with open(filename, 'w') as f:
            json.dump(number, f)
            return True
    except FileNotFoundError:
        return False


def retrieve_user_favorite_number():
    """It retrieves the user's favorite number from the database"""
    try:
        filename = 'fav_num.json'
        with open(filename) as file:
            number = json.load(file)
            user_response = input(f"Is {number} your favorite number? \nEnter Yes or No: ")
            if user_response.lower().strip() == 'no':
                collect_favorite_num()
                print("We'll remember your favorite number when you come back")
            elif user_response.lower().strip() == 'yes':
                print(f"You see i told you i would remember your favorite number!")
            else:
                print("Please enter a valid input")
    except FileNotFoundError:
        collect_favorite_num()


retrieve_user_favorite_number()