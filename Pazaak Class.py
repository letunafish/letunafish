#Objects - Deck, Sidedeck, Card, Player, Game

import random
from xml.etree.ElementTree import ProcessingInstruction


class deck:
    def __init__ (self):
        self.cards = [i%10+1 for i in range(40)]
        random.shuffle(self.cards)
    
    def draw (self):
        return self.cards.pop()
    
    def shuffle (self):
        random.shuffle(self.cards)
    
    def deck_print (self):
        print (self.cards)

    def reset (self):
        self.cards = [i%10+1 for i in range(40)]
        random.shuffle(self.cards)

class side_deck:
    def __init__(self):
        self.cards = [1,-1,2,-2,+3,-3, +4, -4, 1, -1]
        random.shuffle(self.cards)
        self.hand = self.cards[0:4]
    
    def draw (self,index):
        return self.hand.pop(index)

    def side_print (self):
        print (self.hand)

    def custom_sd (self, nuhand):
        self.card = nuhand
        random.shuffle(self.card)
        self.hand = self.card[0:4]

    def reset (self):
        random.shuffle(self.cards)
        self.hand = self.cards[0:4]


class player:
    def __init__(self, flip):
        self.wins = 0
        self.sd = side_deck()
        self.stand = False
        self.points = 0
        self.name = flip

    def game_reset(self):
        self.sd.reset()
        self.points = 0
        self.stand = False

    def do_stand(self):
        wish = input("Do You Wish To Stand? Y/N ")
        if wish == "Y":
            self.stand = True

    def choose_sd(self):
        self.sd.side_print()
        choose = int(input("Choose A Card "))
        return self.sd.draw(choose)
    
    def player_sd(self):
        self.sd.side_print()

    def current_points(self):
        return self.points

    def check_stand(self):
        return self.stand 
    
class game:
    def __init__(self, players):
        self.gameover = False
        self.players = players
        self.turn = 0

    def check_gameover(self):
        counter = 0
       #print(len(self.players))
        total_players = len(self.players)
        for player in self.players:
            #print(player.current_points())
            if player.current_points() > 20:
                counter = counter + 1
            elif player.check_stand():
                counter = counter + 1 
            #print(counter)
            
        if counter == total_players:
            self.gameover = True
    


#skip logic for game 42
#logic for who won game
#turns draw cards/use side cards/stand or not 51


#Class Set
#prompt to create player objects and names
#increment player total / skip or game class
#Pure Pazaak + winner 
#134 set class wins / check winner




player_1 = player("Chungus")
player_2 = player("Dungus")
player_3 = player("Cowabungus")

playaz = [player_1, player_2, player_3]

Round_1 = game(playaz)
print(Round_1.gameover)
Round_1.check_gameover()
print(Round_1.gameover)

player_1.do_stand()
player_2.do_stand()
#player_3.do_stand()

Round_1.check_gameover()
print(Round_1.gameover)




#play_side_deck = side_deck()
#play_side_deck.side_print()
#index = int(input("choose an index "))
#print(play_side_deck.draw(index))


    


#play_deck = deck()
#player_1 = player("dominos")
#print(str(play_deck.draw()))
#player_1.choose_sd()
#player_1.do_stand()


#play_deck.deck_print()
#play_deck.draw()
#play_deck.deck_print()
#play_deck.shuffle()
#play_deck.deck_print()
#play_deck.reset()
#play_deck.deck_print()