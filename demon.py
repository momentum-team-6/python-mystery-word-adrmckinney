# * Computer chooses a word at random (done)
#     * Finds length of that word (done)
#     * Stores all other words of that length (done)
# * User guesses a letter and compare with computer word. If letter exists in computer word, then …next (done)
# * Computer takes that letter and creates word families of every word for every letter position (remembering all previously guessed letters and their positions) (done)
# * Computer looks at longest word family and randomly selects a word (kinda done)

# ---------------------functions----------------------

def debug_demon(computer_word, all_words_of_same_length, matches, computer_letter_list):
    print('computer word: ', computer_word)
    print("computer letters listed: ", computer_letter_list)
    print("Computer Word length: ", len(computer_word))
    print("Total number of demon words: ", len(all_words_of_same_length))
    print("Matches: ", matches)

def display_game(computer_letter_list):
    print("Myster Word: ", " ".join(["_" for letter in range(len(computer_letter_list))]))

# loop over each index in computer_letter_list ["b", "o", "b"] => [0, 1, 2]
def remember_matching_letters(computer_letter_list):
    for index in range(len(computer_letter_list)):
        letter = computer_letter_list[index]
        if guess == letter:
            matches[index] = letter

# filter the word list based on the matches
# def filter_all_words_of_the_same_length(all_words_of_same_length, matches):
#     for word in all_words_of_same_length:
#         if all(words)

def generate_word_families(demon_length, guess, all_words_of_same_length, matches):
    word_families = {}

    for position in range(demon_length):
        words_for_position = []
        for word in all_words_of_same_length:
            letter = word[position]
            if letter == guess:
                words_for_position.append(word)
        word_families[position] = words_for_position
        
    # print(word_families)
    return word_families

def longest_word_family(word_families):
    longest = []
    for position in word_families:
        family = word_families[position]
        if len(longest) < len(family):
            longest = family
    print(f"longest family length: {len(longest)}")
    return longest


# -----------------^^^^-functions-^^^^-----------------


file = open("words.txt", "r")
read_file = file.read().upper().split()


# limit word length 
demon_words = []

for word in read_file:
    if len(word) >= 4 and len(word) <= 6:
        demon_words.append(word)
# print(demon_words)

# computer select a word at random
import random
computer_word = random.choice(demon_words)
demon_length = len(computer_word)

# loop through demon_words, find their length, if length matches computer_word_length append it to word_family
all_words_of_same_length = []
for word in demon_words:
    if len(word) == len(computer_word):
        all_words_of_same_length.append(word)


# convert computer word from string to list.
computer_letter_list = list(computer_word)
# print ('display', computer_word_string_to_list)

debug_demon(computer_word, all_words_of_same_length, {}, computer_letter_list)



display_game(computer_letter_list)


# input request to guess a letter
guess = input(f"Guess a letter ").upper()



# create memory to store user guesses and positions list to store the index value of each computer word
memory_for_guessed_letters = []
memory_for_guessed_letters_position = []
matches = {}

# for every letter that is guessed, loop through word_family_parent and create a new list for words that match the index value of that letter

# capture the matches length
match_length_before = len(matches)
remember_matching_letters(computer_letter_list)
match_length_after = len(matches)

debug_demon(computer_word, all_words_of_same_length, matches, computer_letter_list)

if match_length_before != match_length_after:
    # generate word families from matches
    word_families = generate_word_families(demon_length, guess, all_words_of_same_length, matches)
    # select longest key with the most values (word_family with the longest list)
    word_family = longest_word_family(word_families)
    # random
    computer_word = random.choice(word_family)
    # call display game function
    display_game(computer_word)
    print("*computer word: ", computer_word)

else:
    print("No match fucker")

