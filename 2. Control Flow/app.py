# Guess the Random number between 1 - 100 game
import random
r_number = random.randint(1, 100)
for attempt in range(5):
    user_guess_number = int(input('Type your guess number: '))
    if user_guess_number == r_number:
        print('correct guess')
        break
    else:
        print('wrong guess, try again')

else:
    print('All your guesses are wrong. the number was: ', r_number)
