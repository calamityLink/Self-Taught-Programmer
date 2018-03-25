from random import shuffle

class Card:
    suits = ['spades','hearts','diamonds','clubs']
    values = [None,None,'2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    def __init__(self,v,s):
        #Value and Suit are integers
        self.value = v
        self.suit = s

    def __lt__(self,c2):
        if self.value < c2.value: #We're using the integer version of the less-than operator here.
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False #We only hit this line if self.value < c2.value

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' of ' \
            + self.suits[self.suit]
        return v

##***Test Code***
##card1 = Card(10,2)
##card2 = Card(11,3)
##print(card1 < card2)
##print(card1 > card2)
##print(card1)
##****************

class Deck:
    def __init__(self):
        self.cards = [] ##Deck being represented as list of cards
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

##***Test Code***
##Print the shuffled deck
##deck = Deck()
##for card in deck.cards:
##    print(card)
##***************

class Player:
    def __init__(self,n):
        self.wins = 0
        self.card = None
        self.name = n

class Game:
    def __init__(self):
        n1 = input('Player 1 name: ')
        n2 = input('Player 2 name: ')
        self.deck = Deck()
        self.p1 = Player(n1)
        self.p2 = Player(n2)

    def wins(self,w):
        winmsg = "{} wins this round"
        winmsg = winmsg.format(w)
        print(winmsg)

    def draw(self,p1n,p1c,p2n,p2c):
        drawmsg = '{} drew {}, {} drew {}'
        drawmsg = drawmsg.format(p1n,p1c,p2n,p2c)
        print(drawmsg)

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name + ' wins!'
        if p2.wins > p1.wins:
            return p2.name + ' wins!'
        return 'It was a tie!'
        

    def play_game(self):
        cards = self.deck.cards
        print('Beginning War!')
        while len(cards) >= 2:
            msg = 'q to quit. Any key to play: '
            response = input(msg)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            self.draw(self.p1.name,p1c,self.p2.name,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            if p2c > p1c:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1,self.p2)
        print('War is over. {}'.format(win))

game = Game()
game.play_game()
