def random_game_engine():
    """This function runs a guess game engine where the user
    is expected guess the random number correctly
    by choosing a number between 1 and 1000."""

    print('Welcome to random game engine...a place where you put your guessing abilities into great test. \n')
    random_number = 1 + random.randrange(1000)
    reply = int(input('Guess my number between 1 and 1000 with the fewest guesses:'))
    while reply != random_number:
        random_number = 1 + random.randrange(1000)
        reply = int(input('Guess my number between 1 and 1000 with the fewest guesses:'))
        if reply > random_number:
            print('Too high. Try again.')
        elif reply < random_number:
            print('Too low. Try again.')
        else:
            print('Congratulations. You guessed the number!')
            user_reply = int(input('Would you like to continue this beautiful game? Enter 1 for yes, 2 for no'))
            if user_reply == 1:
                random_game_engine()
            else:
                print('Thank you for your time. see ya...')


random_game_engine()
