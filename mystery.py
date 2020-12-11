file = open('words.txt', 'r')
opened_file = file.read()

upper_list = opened_file.upper().split()

easy_words = []
medium_words = []
hard_words = []
demon_words = []

for word in upper_list:
    if len(word) >= 3 and len(word) <= 5:
        easy_words.append(word)
    if len(word) >=6 and len(word) <=8:
        medium_words.append(word)
    if len(word) >= 9 and len(word) <= 12:
        hard_words.append(word)
    if len(word) >= 13 and len(word) <= 25:
        demon_words.append(word)

print("\U0001F600")


while True:
    difficulty = input('Choose your difficulty level: easy, medium, hard, or demon | ')
    if difficulty != "easy" and difficulty != "normal" and difficulty != "hard" and difficulty != "demon":
        print('\U0001F644 That is not an option.')
        continue
    else:
        break

print('difficult level is:', difficulty)


selected_list = None
if difficulty == "easy":
    selected_list = easy_words
elif difficulty == "medium":
    selected_list = medium_words
elif difficulty == "hard":
    selected_list = hard_words
elif difficulty == "demon":
    selected_list = demon_words

import random
computer_word = random.choice(selected_list)
computer_word_list = [letter for letter in computer_word]
print('computer word is: ', computer_word)



display_word = ['_' for letter in range(len(computer_word))]
print(" ".join(display_word))

positions = []
max_guesses = 8
tries = 0
memory = []

while computer_word_list != display_word and max_guesses > 0:
    guess = input('Guess a letter: ')
    upper_guess = guess.upper()

    if upper_guess == "":
        print("You have to guess a letter")
    
    # elif upper_guess == int or upper_guess == float:
    #     print("You have to guess a letter")
    
    elif upper_guess in memory:
        print(f"You have already tried {upper_guess}")

    elif upper_guess in computer_word_list:
        memory.append(upper_guess)
        for i in range(len(display_word)):
            if upper_guess == computer_word[i]:
                positions.append(i)
                for position in positions:
                    display_word[position] = upper_guess
                    positions = []
        print(f"Yes, {upper_guess} is in the word")
        print(" ".join(display_word))
    else:
        memory.append(upper_guess)
        max_guesses -= 1
        print(f"{upper_guess} is not in word. You have {max_guesses} guesses left")


if computer_word_list == display_word:
    print("\U0001F604 A WINNER IS YOU \U0001f600")
else:
    print(f"\U0001F643 LOSER \U0001F923 The word was {computer_word}. Better luck next time")