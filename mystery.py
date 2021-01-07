# User prompt to chose between memory game or number guess
# game_choice = input("Select which game you would like to play, Mystery Word or Guess the Number | ")

# if game_choice == "Mystery Word":
#     mystery_word()
# if game_choice == "Guess the Number":
#     pass


# Function start for memory game
# def mystery_word(Mystery_Word):
    # start_mystery_game = open('words.txt', 'r')
    # opened_file = start_mystery_game.read()

import random

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
    if len(word) >= 6 and len(word) <= 25:
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

demon_mode = False
selected_list = None
if difficulty == "easy":
    selected_list = easy_words
elif difficulty == "medium":
    selected_list = medium_words
elif difficulty == "hard":
    selected_list = hard_words
elif difficulty == "demon":
    selected_list = demon_words
    demon_mode = True

# print('demon word', demon_words)


computer_word = random.choice(selected_list)
# computer_word = "ZOUNDS"
computer_word_list = [letter for letter in computer_word]
print('computer word is: ', computer_word)

#------------------ code for demon words-------------------------
# word families = words of the same length
computer_word_length = len(computer_word_list)
print('length', computer_word_length)

# any word in demon_words that has the same length. Create a word_family list
word_family = []

# loop through demon_words, find their length, if length matches computer_word_length append it to word_family
for word in demon_words:
    demon_word_length = len(word)
    if len(word) == computer_word_length:
        word_family.append(word)
# print('word family', word_family)

# With similar length demon words inside word_family, now I need to check when the user chooses a correct letter, find that letters index in the selected word, and compare the word_family list to that index value for that letter. 

def generate_demon_list(letter_positions, word_length, word_family):
    filtered_list = []
    # filter all of the words in the word family that match the letter
    # position



# All words that share that letter index value should be grouped into a new list. So just reset word_family and put the new list inside it. Or maybe .remove ever word that is not that index point.

#------------------ code for demon words-------------------------   

display_word = ['_' for letter in range(len(computer_word))]
print(" ".join(display_word))

positions = []
max_guesses = 8
memory = []

while computer_word_list != display_word and max_guesses > 0:
    game_display = "Guess a letter 👹: " if demon_mode else "Guess a letter: "

    guess = input(game_display)
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
        print("")
        print("Used letters: ", " ".join(memory))
        print("Word: ", " ".join(display_word))
        print("")
    else:
        memory.append(upper_guess)
        max_guesses -= 1
        print("")
        print(f"{upper_guess} is not in word. You have {max_guesses} guesses left")
        print("Used letters: ", " ".join(memory))
        print("Word: ", " ".join(display_word))
        print("")


if computer_word_list == display_word:
    print("\U0001F604 A WINNER IS YOU \U0001f600")
else:
    print(f"\U0001F643 LOSER \U0001F923 The word was {computer_word}. Better luck next time")


# build a second game inside this. Make a function for mystery game and a function for guess the number