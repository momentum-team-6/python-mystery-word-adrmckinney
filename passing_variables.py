# number = 0
# my_list = []

# def build_list(letter_list):
#     new_list = letter_list.copy()
#     letter_list.append("A")
#     print(id(letter_list))
#     print("new list id: ", id(new_list))
#     print(letter_list)

# build_list(my_list)

# def increase_number(num):
#     num += 1 #same as num = num + 1
#     print(num)

# increase_number(number) #this is passing in the global "number" into the function for the value of "num"

# blackJack
SUITS = ["♣️", "❤️", "♦️", "♠"]
RANKS = ["A", "J", "Q", "K", 2, 3, 4, 5, 6, 7, 8, 9, 10]

class Card:
    def __init__(self, suit, rank):  #init method is the blueprint for what will happen in the object; "self" is the "instance"
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"card is a {self.rank} of {self.suit}"

class Deck:
    def __init__(self, suits, ranks, color):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.color = color
    
    def deal(self):
        '''gives two cards to each player and dealer'''
        pass
    


my_deck = Deck(SUITS, RANKS)
for card in my_deck.cards:
    # print(card)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def __str__:(self):
        return f"{self.name} is holding {self.hand}"


class Dealer(Player):   #inheritance. We subclassed player for dealer, giving Dealer the methods of Player
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
    
    def __str__(self):
        
        return f"{self.color} deck"

class Game:
    def __init__(self, deck_color):
        self.player = Player(self.welcome())
        self.dealer = Dealer()
        self.deck = Deck(SUITS, RANKS, deck_color)
        self.winner = None
    
    def welcome(self):
        player_name = input("Welcome to blackjack! What is your name? ")
        return player_name

new_game = Game("blue")
