import random

def guess(x):
    random_number = random.randint(1,x);
    guess = 0;
    while(guess != random_number):
        guess = int(input(f'Enter number to guess between 1 and {x}: '));
        if(guess < random_number):
            print(f'your number {guess} is too low')
        elif(guess>random_number):
            print(f'your number {guess} is too high')

    print(f'your found the number  {random_number}')

guess(10)