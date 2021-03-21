def is_palindrome(arg: str) -> bool:
    if arg == arg[::-1]:
        return True
    else:
        return False


print(is_palindrome(input("Welcome to palindrome checker!\nKindly enter a string: ")))