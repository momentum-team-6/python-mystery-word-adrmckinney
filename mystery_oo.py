import random

class Game:
    def __init__(self):
        self.word = self.setup_word()
        self.memory = []
        self.turns_remaining = 6
        self.guessed_word = None
        

    def setup_word(self):
        
        while True:
            difficulty = input("Wecome to the Mystery Word game. What difficulty level would you like: Easy, Medium, Hard, or Demon? ").lower()
            if difficulty != "easy" and difficulty != "medium" and difficulty != "hard" and difficulty != "demon":
                print("\nThat is not an option. Please try again…\n")
            else:
                break

        setup_length = None
        if difficulty == "easy":
            setup_length = random.choice(range(3, 6))
        if difficulty == "medium":
            setup_length = random.choice(range(7, 10))
        if difficulty == "hard":
            setup_length = random.choice(range(11, 20))
        if difficulty == "demon":
            setup_length = random.choice(range(6, 8))
        
        cheat_mode = input("Are you a cheater? (y/n) ").lower() == "y"

        if difficulty == "demon":
            return DemonWord(setup_length, cheat_mode)
        else:
            return Word(setup_length, cheat_mode)


    def play(self):
        print("\nmystery word: ", self.word.output())
        while self.turns_remaining != 0 and not self.word.guessed_correctly():
            print("\nGuessed letters: ", " ".join(self.memory))
            guessed_letter = input("\nGuess a letter: ").upper()
            print("\n–––––––––––––––––––––––––––––––––––––––––––––––––––")
            
            if guessed_letter in self.memory:
                print("You have already guessed this letter")
                print(f"You still have {self.turns_remaining} guesses left")
                print("\nmystery word: ", self.word.output())
            else:
                self.memory.append(guessed_letter)
                positions_before_guess = dict(self.word.show_positions())

                positions_after_guess = self.word.guess(guessed_letter)
                if positions_after_guess == positions_before_guess:
                    self.turns_remaining -= 1
                    print(f"\n{guessed_letter} is not in the word.")
                else:
                    print(f"\nYes, {guessed_letter} is in the word!")
                
                print(f"\nYou have {self.turns_remaining} wrong guesses left\n")
                print("\nmystery word: ", self.word.output())

        if self.word.guessed_correctly():
            print("\nA WINNER IS YOU!")
            self.play_again()
        else:
            print(f"\nYou lost. The word was {self.word.computer_word}")
            self.play_again()
        
    def play_again(self):
        replay = input("\nWould you like to play again? (y/n) ").lower()
        print("\n\n\n")
        if replay == "y":
            new_game = Game()
            new_game.play()
        else:
            print("Thanks for playing")

class Word():
    def __init__(self, setup_length, cheat_mode):
        self.setup_length = setup_length
        self.positions = {}
        self.words_of_matching_length = []
        self.computer_word = self.random_word()
        self.cheat_mode = cheat_mode
        
        
    def output(self):
        if self.cheat_mode:
            print("\nComputer Word:", self.computer_word)


        output = []
        for index in range(len(self.computer_word)):
            if index in self.positions and self.positions[index] == list(self.computer_word)[index]: # does the key exist in positions and does the value of the index match
                output.append(list(self.computer_word)[index])
            else:
                output.append("_")
        return " ".join(output)

    def list_of_same_length_words(self):
        file = open("words.txt", "r")
        all_words = file.read().upper().split()
        
        for word in all_words:
            if len(word) == self.setup_length:
                self.words_of_matching_length.append(word)
        return self.words_of_matching_length    

    def random_word(self):
        return random.choice(self.list_of_same_length_words())

    def length(self):
        return self.setup_length

    def show_positions(self):
        return self.positions
    
    def guess(self, guessed_letter):
        for index in range(len(self.computer_word)):
            if guessed_letter == self.computer_word[index]:
                self.positions[index] = guessed_letter
            
        return self.positions

    def guessed_correctly(self):
        if len(self.positions) == len(self.computer_word):
            return True
        else:
            return False

class DemonWord(Word):
    def __init__(self, setup_length, cheat_mode):
        super().__init__(setup_length, cheat_mode)
        self.demon_dict = {}
        self.demon_word_list = self.list_of_same_length_words()
        self.letter_filters = []
        self.word_memory = []

    def output(self):
        if self.cheat_mode:
            print(f"demon word list has {len(self.demon_word_list)} words\n")
            print(self.demon_word_list[:10])
            print("positions: ", self.positions)
            print("letter filters: ", self.letter_filters)
            print("Words the computer has selected: ", self.word_memory)
            # print("Letter filters ", self.letter_filters)
            # print("longest word family: ", len(longest_word_family))

        return f"👹 {super().output()}"  #super is the super class, Word, I'm saying return whatever is normally returned in Word with the addition of my cool emoji.

    def remove_words_wrong_guess(self):
        unfiltered_words = []

        for word in self.demon_word_list:
            letter_filter_not_found = True # this sets the current word in demon word list to be included by default

            # if we find a filtered letter in a word, mark it as not included in unfiltered_words
            for letter in self.letter_filters:
                if letter in word:
                    letter_filter_not_found = False

            # if word not marked to be excluded, then append to unfiltered_words
            if letter_filter_not_found:
                unfiltered_words.append(word)

        self.demon_word_list = unfiltered_words
        # self.computer_word = random.choice(self.demon_word_list)
        # self.word_memory.append(self.computer_word)
    
    def remove_words_correct_guess(self):
        '''Old Code using dict positions'''
        unfiltered_words = []

        for word in self.demon_word_list:
            if self.allow_word_for_positions(word):
                unfiltered_words.append(word)

        self.demon_word_list = unfiltered_words
        '''Old Code using dict positions'''

        '''New code comparing against output to remove words'''
        # unfiltered_words = []

        # for position in range(len(self.output())):
        #     for word in self.demon_word_list:
        #         for letter in word[position]:
        #             if letter == self.output()[position]:
        #                 unfiltered_words.append(word)
        
        # self.demon_word_list = unfiltered_words
        

    def allow_word_for_positions(self, word):
        if len(self.positions) == 0:
            return True
        include_word = True

        for position in self.positions:
                comparison_letter = self.positions[position]
                if word[position] != comparison_letter:
                    include_word = False
        return include_word

    def guess(self, guessed_letter):
        self.word_memory.append(self.computer_word)
        if guessed_letter in list(self.computer_word):
            word_families = {}
            
            # generate new demon word families
            for position in range(len(self.computer_word)):
                words_for_position = []
                for word in self.demon_word_list:
                    letter = word[position]
                    if letter == guessed_letter and self.allow_word_for_positions(word):
                        words_for_position.append(word)
                word_families[position] = words_for_position
            
            longest_word_family = []
            for key in word_families:
                if len(word_families[key]) > len(longest_word_family):
                    longest_word_family = word_families[key]
                
            self.computer_word = random.choice(longest_word_family)
            self.demon_word_list = longest_word_family
            ''' remove words with guessed letter from demon word list '''

            self.remove_words_correct_guess()

        else:
            # print(f"{guessed_letter} is not in the word.", guessed_letter)
            self.letter_filters.append(guessed_letter)
            self.remove_words_wrong_guess()

        
        return super().guess(guessed_letter)
        
new_game = Game()
new_game.play()
