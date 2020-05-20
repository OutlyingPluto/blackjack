import random
class Game():

    #CLASS ATTRIBUTE ELEMENTS
    deck = [['#', '#', '2-H', '3-H', '4-H', '5-H', '6-H', '7-H', '8-H', '9-H', '10-H', 'Jack-H', 'Queen-H', 'King-H', 'Ace-H'], ['#', '#', '2-D', '3-D', '4-D', '5-D', '6-D', '7-D', '8-D', '9-D', '10-D', 'Jack-D', 'Queen-D', 'King-D', 'Ace-D'], ['#', '#', '2-S', '3-S', '4-S', '5-S', '6-S', '7-S', '8-S', '9-S', '10-S', 'Jack-S', 'Queen-S', 'King-S', 'Ace-S'], ['#', '#', '2-C', '3-C', '4-C', '5-C', '6-C', '7-C', '8-C', '9-C', '10-C', 'Jack-C', 'Queen-C', 'King-C', 'Ace-C']]
    total_amount = 0
    bet_amount = 0
    player_total = 0
    computer_total = 0
    player_cards = []
    comp_cards = []
    status = True

    def __init__(self):
        pass


    def start_game(self):
        
        #GAME STARTS, RANDOM CARDS ARE GENERATED

        print('Welcome to BlackJack!\n\n')
        Game.total_amount = int(input('How much betting amount do you have?  ')) 
        print('\n')
        self.place_bet()
        print('\n\n')
        self.game_start()
        while Game.status == True:
            self.hit()
            if self.check_bust():
                break
        if Game.status == False:
            self.computer_moves()
        
            
        
    def place_bet(self):
        
        #CHECKS IF A PLAYER HAS ENOUGH BUDGET TO BET

        while True:
            Game.bet_amount = int(input('How much bet do you want to place?  '))
            if Game.bet_amount > Game.total_amount:
                print("Short of money...")
                continue
            else:
                break


    def game_start(self):

        #SHOWS GAME STATUS IN FIRST TURN

        self.draw_card_comp()
        print(f"Computer has {self.draw_card_comp()} and a hidden card\n")
        print(f"Your cards: {self.draw_card_player()} and {self.draw_card_player()}")
        print(f"Total: {Game.player_total}")


    def game_status(self):

        #SHOWS GAME STATUS AFTER FIRST TURN

        print(f"Computer has {' '.join(Game.comp_cards)} and a hidden card")
        print(f"Your cards: {', '.join(Game.player_cards)}")
        print(f"Total: {Game.player_total}")

    
    def draw_card_comp(self):

        #DRAWS CARDS FOR COMPUTER

        while True:
            rand_index1 = Game.deck[random.randint(0, 3)]
            rand_index2 = random.randint(2, 14)
            if not self.card_available(rand_index1, rand_index2):
                continue
            if rand_index2 == 14:
                computer_total += self.computer_ace(rand_index1, rand_index2)
                Game.comp_cards.append(rand_index1[rand_index2])
                return self.card_remove(rand_index1, rand_index2)                
            elif rand_index2 > 10 and rand_index2 < 14:
                Game.computer_total += 10
                Game.comp_cards.append(rand_index1[rand_index2])
                return self.card_remove(rand_index1, rand_index2)                
            else:
                Game.computer_total += rand_index2
                Game.comp_cards.append(rand_index1[rand_index2])
                return self.card_remove(rand_index1, rand_index2)                
            break


    def draw_card_player(self):
        
        #DRAWS A RANDOM CARD AND CHANGES IT TO 0
        
        while True:
            rand_index1 = Game.deck[random.randint(0, 3)]
            rand_index2 = random.randint(2, 14)
            if not self.card_available(rand_index1, rand_index2):
                continue
            if rand_index2 == 14:
                Game.player_total += self.ace_card()
                Game.player_cards.append(rand_index1[rand_index2])
                return self.card_remove(rand_index1, rand_index2)                
            elif rand_index2 > 10 and rand_index2 < 14:
                Game.player_total += 10
                Game.player_cards.append(rand_index1[rand_index2])
                return self.card_remove(rand_index1, rand_index2)               
            else:
                Game.player_total += rand_index2
                Game.player_cards.append(rand_index1[rand_index2])
                return self.card_remove(rand_index1, rand_index2)               
            break


    def ace_card(self):
    
        #ASK FOR A VALUE IF CARD IS ACE
       
        ace_value = 0
        while ace_value != 1 and ace_value != 11:
            ace_value = int(input("You've recieved an Ace! What value do you want?(1/11)  "))
        return ace_value


    def card_available(self, symbol, index):

        #CHECKS IF A CARD IS AVAILALBLE IN Game AND RETURNS BOOLEAN
        return not symbol[index] == 0 


    def card_remove(self, symbol, index):
        
        #REMOVES A CARD FORM Game

        thecard = symbol[index]
        symbol[index] = 0
        return thecard
        

    def hit(self):

        #ASKS TO EITHER HIT OR STAND

        while True:
            hit_or_stand = input("Hit or Stand?  ").lower()
            if hit_or_stand == 'hit':
                self.draw_card_player()
                self.game_status()
                break
            elif hit_or_stand == 'stand':
                Game.status = False
                break
            else:
                continue


    def check_bust(self):

        #CHECK IF THERE IS A BUST

        if Game.player_total > 21:
            print('BUST!!! You LOST')
            return True

    
    def computer_ace(self, symbol, index):

        #CHECKS IF A COMPUTER GETS ACE

        if computer_total + 11 > 21:
            return 1
        else:
            return 11


    def computer_moves(self):
        
        #ALLOWS COMPUTER TO PLAY MOVES UNTIL HIS TOTAL EXCEEDS PLAYER'S TOTAL
        
        while Game.computer_total < Game.player_total:
            self.draw_card_comp()
            if Game.computer_total == Game.player_total >= 17:
                print(f"\nComputer's Total: {Game.computer_total}")
                print('Computer takes a stand!')
                print('DRAW!')
                Game.status = True
                break
        if Game.status == False:
            if Game.computer_total <= 21:
                print(f"\nComputer's Total: {Game.computer_total}")
                print('Computer Won!')
            elif Game.computer_total > 21:
                print(f"\nComputer's Total: {Game.computer_total}")
                print('Computer BUSTED! You Won!')



if __name__ == '__main__':
    Game1 = Game()
    Game1.start_game()

