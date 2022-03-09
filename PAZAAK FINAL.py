## 0. draw four side cards
# 1. player draws a card from main deck
## 2. choose to play side card or pass
## 3. check to see if score >= 20 if yes end game
## 4. loop back to (1)

import random

setOver = False
setWinner = ""

p1wins = 0
p2wins = 0
 
p1sd = [1,-1,2,-2,+3,-3, +4, -4, 1, -1]
p2sd = [1,-1,2,-2,+3,-3, +4, -4, 1, -1]

random.shuffle(p1sd)
random.shuffle(p2sd)

hand1 = p1sd[0:4] # p1 draws 4 cards
hand2 = p2sd[0:4] # p2 draws 4 cards

while (not setOver):
    deck = [i%10+1 for i in range(40)] 
    #print (deck)
    gameOver = False
    gameWinner = ""
    skip1 = 0
    skip2 = 0
    p1Total = 0
    p2Total = 0


    random.shuffle(deck)



    #while
    turn = 1
    while (not gameOver):
        if skip1==1 and skip2==1:
            if p1Total > p2Total:
                gameWinner = "p1"
            elif p2Total > p1Total:
                gameWinner = "p2"
            else:
                gameWinner = "draw"
            gameOver = True
            break
        if turn % 2 == 1: 

            print("\nPlayer 1's turn")
            print(hand1)
            card = deck.pop()
            print(card)
            p1Total = p1Total + card
            print("\nYour total is: " + str(p1Total))
            decision = input("\nDo you wish to pass (p) or play sidecard (s)?")
            if decision == "p":
                pass 
            elif decision ==  "s":
                print(hand1)
                index = int(input("\nWhich card to playy (0-3)").strip())
                p1Total = p1Total + hand1.pop(index)
                print(p1Total)

            if p1Total > 20:
                gameOver = True
                gameWinner = "p2"
            elif p1Total == 20:
                #gameOver = True
                #gameWinner = "p1"
                skip1 = 1
                turn = turn  +1 + skip2 #skip1 + 1
            else:
                stand = input("\nDo you wish to stand? (y/n)")
                if stand == 'y':
                    print("\nplayer 1 stands")
                    skip1 = 1
                    turn = turn  +1 + skip2 #skip1 + 1

                else:
                    turn = turn + skip2 + 1
        
                

        else:
            print("\nPlayer 2's turn")
            print(hand2)
            card = deck.pop()
            print(card)
            p2Total += card
            print("\nYour total is: " + str(p2Total))
            decision = input("\nDo you wish to pass (p) or play sidecard (s)?")

            if decision == "p":
                pass
            elif decision == "s":
                print(hand2)
                index = int(input("\nWhich card to playy (0-3)").strip())
                p2Total += hand2.pop(index)
                print(p2Total)

            if p2Total > 20:
                gameOver = True
                gameWinner = "p1"
            elif p2Total == 20:
                #gameOver = True
                #gameWinner = "p2"
                skip2 = 1
                turn = turn  +1 + skip1

            else:
                stand = input("\nDo you wish to stand? (y/n)")
                if stand == 'y':
                    print("\nplayer 2 stands \n")
                    skip2 = 1
                    turn = turn + 1 + skip1
                else:
                    turn = turn + skip1 + 1
            
    if gameWinner == "p1":
        p1wins += 1
    elif gameWinner == "p2":
        p2wins += 1
    
    
    print(gameWinner)
    print("\n p1 has " + str(p1wins))
    print("\n p2 has " + str(p2wins))

   
    if p1wins == 3:
        setWinner = "Player 1"
        setOver = True 
    elif p2wins == 3:
        setWinner = "Player 2"
        setOver = True

print("\n" + str(setWinner) + " is the winner!")
print("\nThat's PURE pazaak ;)")







