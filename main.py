import random
from IPython.display import clear_output

class Deck():
    def __init__(self):
        self.deck = []

    def make_deck(self):
        ranks = (['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

        for rank in range(len(ranks)):
            temp = (ranks[rank])
            self.deck.append(temp)

        random.shuffle(self.deck)
        return self.deck


class Blackjack(Deck):
    def __init__(self, deck, play):
        self.deck = deck
        self.play = play

    def theInstructions(self):
        print('Welcome to Blackjack!')
        print('-------♠ ♡ ♢ ♣-------')
        print('Think you can beat a computer?')
        print('How to play:')
        print('1. Have a higher score than me to win.')
        print('2. Going over a value of 21 is called a \'bust\', which results in an automatic loss.')
        print('3. I have to draw a card if I have under 17 points.')
        print('4. If we tie, it\'s called a \'push\'')
        print('5. Type \'hit\' to draw a card or \'stay\' to end your turn.')

    def startGame(self, players):
        for player in players:
            player.getCard(self.draw())
            player.getCard(self.draw())

    def draw(self):
        card = self.deck[0]
        del self.deck[0]
        return card

    def showHands(self, player, dealer):
        pc = player.sumHands()
        dc = dealer.sumHands()

        print(f'Dealer\'s Hand\t Total: {dc}.')
        print('[X]')
        for card in range(1,len(dealer.hand)):
            print(f'[{dealer.hand[card]}]')



        print(f'Player\'s Hand\t Total: {pc}.')
        for card in range(1,len(player.hand)):
            print(f'[{player.hand[card]}]')


class Player():
    def __init__(self, tag):
        self.tag = tag
        self.hand = []
        self.is_bust = False

    def getCard(self, card):
        self.hand.append(card)

    def sumHands(self):
        total = 0
        ace = False
        for card in self.hand:
            if type(card) == int:
                total += card
            elif card == 'J' or card == 'Q' or card == 'K':
                total += 10
            elif card == 'A':
                ace = True
                if (total + 11) > 21:
                    total += 1
                else:
                    total += 11

        if total > 21 and ace == True:
            for card in self.hand:
                if card[0] == 'A':
                    total -= 10
        return total

# [total += card[0] if card[0] == int else total += 10 if card[0] != 'A' and == str else total += 1 if card[0] == 'A' and (total + 11) > 21 else total += 11 for card in self.hand]

def loseCondition(player, dealer):
    if player.is_bust == True:
        print('You busted!')
    elif dealer.sumHands() <= 21 and dealer.sumHands() > player.sumHands():
        print(f'Dealer Sum: {dealer.sumHands()}')
        print(f'Player Sum: {player.sumHands()}')
        print('You lost to the dealer!')
    else:
        return False


def winCondition(player, dealer):
    if player.sumHands == 21:
        print('You win!')
    elif player.sumHands() <= 21 and player.sumHands() > dealer.sumHands():
        print(f'Dealer Sum: {dealer.sumHands()}')
        print(f'Player Sum: {player.sumHands()}')
        print('You won!')
    else:
        return False


def dealerTurn(player, dealer, game):
    clear_output()
    game.showHands(player, dealer)

    if player.is_bust == False:
        while True:
            if dealer.sumHands() < 17:
                clear_output()
                dealer.getCard(game.draw())
                # if the dealer hits show the cards again
                game.showHands(player, dealer)
            else:
                break

def playerTurn(player, dealer, game):
    clear_output()
    game.showHands(player, dealer)

    while True:
        if player.sumHands() == 21:
            print('You got Blackjack!')
            return False
        user_input = input('Would you like to HIT or STAY?')
        clear_output()
        if user_input.lower() == 'stay':
            return False
        elif user_input.lower() == 'hit':
            player.getCard(game.draw())
        else:
            print('Not a valid entry! Type HIT or STAY!')

        game.showHands(player, dealer)


def playAgain(self):
    user_input = input('Would you like to play again? YES or NO?')
    if user_input.lower() == 'no':
        print('Thanks for playing!')
        return False
    if user_input.lower() == 'yes':
        startGame()
    else:
        print('Not a valid entry! Type YES or NO!')

    if player.sumHands() > 21:
        player.is_bust = True




##############################################
##############################################
##############################################


while True:
    print('Are you ready to play Blackjack?')
    user_input = input('Type p to play or q to quit')
    if user_input.lower() == 'q' or user_input.lower() == 'quit':
        break
    else:
        d = Deck()
        d.make_deck()
        game = Blackjack(d.deck, 'Blackjack')
        dealer = Player("Dealer")
        player = Player("Player")
        players = [dealer, player]
        flag = True
        while flag:
            clear_output()
            game.startGame(players)
            game.theInstructions()
            game.showHands(player, dealer)
            playerTurn(player, dealer, game)
            dealerTurn(player, dealer, game)
            loseCondition(player, dealer)
            winCondition(player, dealer)
            break
