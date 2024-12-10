import random

random_number = random.randint(1,10)

user_guess = input('Guess a number between 1 and 10: ')

if int(user_guess) == random_number:
    print(f'Well done, you guessed the correct number of {random_number}')
else:
    print(f'Bad luck! The correct number was {random_number}')