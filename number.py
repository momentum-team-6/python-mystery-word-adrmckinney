print("")
print("Welcome to the game where I think of a number between 1–100 and you have to try to guess that number")
print("")
while True:
    difficulty = input("Choose your difficulty level: easy, medium, hard, or impossible | ")
    if difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "impossible":
        print('That is not an option. Please try again.')
        continue
    else:
        break
print("")


import random
computer_number = random.randrange(1, 101)
# print(computer_number)

easy_counter = 10
medium_counter = 8
hard_counter = 5
impossible_counter = 3

counter = 0

if difficulty == "easy":
    counter += easy_counter
if difficulty == "medium":
    counter += medium_counter
if difficulty == "hard":
    counter += hard_counter
if difficulty == "impossible":
    counter += impossible_counter


guess = []
print(f"You selected the {difficulty} difficulty level.")
print(f"You have {counter + 1} guesses")

while guess != computer_number:
    print("")
    guess = int(input("Guess the number I am thinking of: "))
    if counter == 0:
        print("")
        print(f"You are out of guesses. The number I was think of was {computer_number}")
        break
    elif guess < computer_number:
        print("")
        print(f"Your number is too low. You have {counter} guesses left.")
        print("")
        counter -= 1
    elif guess > computer_number:
        print("")
        print(f"Your number is too high. You have {counter} guesses left.")
        print("")
        counter -= 1
    else:
        print("")
        print('You guessed it!')