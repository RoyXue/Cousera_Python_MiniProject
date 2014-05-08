# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card = []	# create Hand object

    def __str__(self):
        str_card = " "
        for i in range(0, len(self.card)):
            str_card += str(self.card[i]) + " "
        return "Hand contains" + str_card	# return a string representation of a hand

    def add_card(self, card):
        self.card.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        sum = 0
        for i in range(0, len(self.card)):
            sum += VALUES[self.card[i].get_rank()]
        
        for i in range(0, len(self.card)):
            if (self.card[i].get_rank() == 'A'): # compute the value of the hand, see Blackjack video
                if sum <= 11:
                    sum += 10
        return sum
   
    def draw(self, canvas, pos):
        for i in range(0, len(self.card)):    # draw a hand on the canvas, use the draw method for cards
            pos[0] = pos[0] + 50
            self.card[i].draw(canvas, pos)
        
# define deck class
class Deck:
    
    def __init__(self):
        self.deck = []	# create a Deck object
        for i in ('C', 'S', 'H', 'D'):
            for n in ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'):
                self.deck.append(Card(i, n))
         
    def shuffle(self):
        random.shuffle(self.deck)	# shuffle the deck 
                                    # use random.shuffle()

    def deal_card(self):
        return self.deck.pop(-1)	# deal a card object from the deck
    
    def __str__(self):
        str_deck = " "
        for i in range(0, len(self.deck)):
            str_deck += str(self.deck[i]) + " "	# return a string representing the deck
        return str_deck


#define event handlers for buttons
def deal():
    global outcome, in_play, score
    global player, dealer, deck 
    player = Hand()
    dealer = Hand()
    deck = Deck()
    deck.shuffle()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    outcome = "hit or deal?"
    if in_play:
        score -= 1
    # your code goes here
    
    in_play = True

def hit():
    global player, deck, outcome, score, in_play# replace with your code below
    if in_play:
        player.add_card(deck.deal_card())
    # if the hand is in play, hit the player
        if (player.get_value() > 21):
            outcome = "Player busted!!!"
            in_play = False
            score -= 1
            print player.get_value()
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, score, in_play
    global dealer, player, score
    if in_play:# replace with your code below
        while dealer.get_value() < 17 :
            dealer.add_card(deck.deal_card())
        if dealer.get_value() > 21 :
            outcome = "Dealer busted!!!"
            in_play = False
            score += 1
        elif dealer.get_value() >= player.get_value():
            outcome = "Dealer wins!!!"
            score -= 1
            in_play = False
        elif dealer.get_value() < player.get_value():
            outcome = "Player wins!!!"
            score += 1
            in_play = False
                    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

                    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    global outcome, score, player, dealer	
    show_score = "Score : " + str(score)
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', [190, 80], 60, 'Purple')
    canvas.draw_text("Dealer's Hand", [50, 150], 40, 'Black')
    canvas.draw_text("Player's Hand", [50, 350], 40, 'Black')
    canvas.draw_text(show_score, [400, 150], 30, 'White')
    canvas.draw_text(outcome, [50, 550], 30, 'Red')
    dealer_pos = [50, 180]
    player_pos = [50, 380]
    player.draw(canvas, player_pos)
    dealer.draw(canvas, dealer_pos)
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
