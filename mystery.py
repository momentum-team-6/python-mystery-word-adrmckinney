file = open('words.txt', 'r')
opened_file = file.read()

upper_list = opened_file.upper().split()

import random
computer_word = random.choice(upper_list)
computer_word_list = [letter for letter in computer_word]
print('computer word is: ', computer_word)

# set difficulty
for word in upper_list:
    if len(word) == 4:
        print(word)


display_word = ['_' for letter in range(len(computer_word))]
print(display_word)

positions = []
max_guesses = 8
tries = 0

while computer_word_list != display_word and max_guesses > 0:

    guess = input('Guess a letter: ')
    upper_guess = guess.upper()
    print(upper_guess)
    if upper_guess in computer_word_list:

        for i in range(len(display_word)):
            if upper_guess == computer_word[i]:
                positions.append(i)
                print(f"Yes, {upper_guess} is in the word")
                for position in positions:
                    display_word[position] = upper_guess
                    positions = []
                    print(display_word)
    else:
        max_guesses -= 1
        print(f"{upper_guess} is not in word. You have {max_guesses} more")
