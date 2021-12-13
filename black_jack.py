#  This code does NOT have User Input Validation

import random
import itertools

class Deck():
    def __init__(self):
        self.clubs = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11', 'c12', 'c13']
        self.dimonds = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd11', 'd12', 'd13']
        self.hearts = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'h10', 'h11', 'h12', 'h13']
        self.spades = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 's11', 's12', 's13']
        self.deck = list(itertools.chain(self.clubs, self.dimonds, self.hearts, self.spades))

class Cards():
    def __init__(self):
        self.players_cards = None
        self.dealers_cards = None

    def add_cards(self, add_list):
        return sum(list(list(map(lambda x: int(x[1:]), add_list))))
    
    def deal_two_cards(self, d):
        new_deck = d
        self.players_cards = [d[0], d[1]]
        self.dealers_cards = [d[2], d[3]]
        del new_deck[0:4]
        return new_deck

    def hit(self, d):
        self.players_cards.append(d[0])
        del d[0]

class Main:
    def run():
        print("""PRESS 1 for 'Hit'
PRESS 2 for 'Stand'
PRESS 3 for 'Play Again'
PRESS 4 for 'Quit'""")
        while True:
            play = Deck()
            cards = Cards()
            random.shuffle(play.deck)
            
            new_deck = cards.deal_two_cards(play.deck)
            
            print(f"""Your cards: {cards.players_cards}
Dealers cards: {cards.dealers_cards[1]} + one face down """)
            if cards.add_cards(cards.players_cards) == 21:
                if input("Blackjack. Play Again or Quit? ") == '3':
                    continue
                else:
                    break
            elif cards.add_cards(cards.players_cards) > 21:
                if input("Bust. Play Again or Quit? ") == '3':
                    continue
                else:
                    break
            
            option = "0"
            while cards.add_cards(cards.players_cards) <= 21:
                if input("Hit or Stand? ") == "2":
                    print(f"Dealers cards: {cards.dealers_cards}")
                    if cards.add_cards(cards.dealers_cards) > 21:
                        option = input("Dealer has Bust. You Win. Play Again or Quit? ")
                        break
                    elif cards.add_cards(cards.players_cards) > cards.add_cards(cards.dealers_cards):
                        option = input("You Win. Play Again or Quit? ")
                        break
                    elif cards.add_cards(cards.players_cards) < cards.add_cards(cards.dealers_cards):
                        option = input("You Lose. Play Again or Quit? ")
                        break
                    else:
                        option = input("Tie. Play Again or Quit? ")
                        break
                else:
                    cards.hit(new_deck)
                    print(f"Your cards: {cards.players_cards}")

            if option == "3":
                continue
            elif option == "4":
                break
            else:
                if input("Bust. Play Again or Quit? ") == '3':
                    continue
                else:
                    break

Main.run()