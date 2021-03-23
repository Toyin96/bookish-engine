def greet_user(user_name="today!"):
    """This function greets the caller by requesting the caller's name
    It has a default value called 'today' which triggers when no argument was entered."""
    default = user_name
    print(f"Hello, {default}")


greet_user()


def display_message():
    """This functions tells the user
    what i'm currently learning in the current chapter."""
    print("I'm currently in chapter 8: 'Python function'")


display_message()