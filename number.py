

import random
computer_number = random.randrange(1, 101)
print(computer_number)

guess = []
counter = 0

while guess != computer_number:
    guess = int(input("Guess the number I am thinking of: "))
    if counter == 5:
        print(f"You are out of guesses. The number I was think of was {computer_number}")
        break
    elif guess < computer_number:
        print('your number is too low')
        counter += 1
        print('counter: ', counter)
    elif guess > computer_number:
        print('your number is too high')
        counter += 1
        print('counter: ', counter) 
    else:
        print('you guessed it!')