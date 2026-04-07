import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < random_number:
            print('too low... try again!')
        elif guess > random_number:
            print('too high... try again!')
    
    print(f'congrats: you are gusseing the number {random_number} correctly!')

guess_number(100)
