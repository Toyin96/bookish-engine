def fizzbuzz_game():
    for number in range(3, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz {number}")
        elif number % 3 == 0:
            print(f"Fizz {number}")
        elif number % 3 == 0:
            print(f"Buzz {number}")


fizzbuzz_game()