import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}
status = True
value = 0
dealervalue = 0
player_hand = []
dealer_hand = []
budget = 0
bet = 0



class Card():

    #MAKES A CLASS OF EACH CARD IN THE DECK

    def __init__(self, suit, rank):
        
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"
        


class Deck():

    #CREATES A DECK, SHUFFLES IT AND SHOWS THE DECK

    deck = []

    
    def __init__(self):
        pass
    

    def create_deck(self):
        for suit in suits:
            for rank in ranks:
                Deck.deck.append(Card(suit, rank))

    def shuffle_deck(self):
        random.shuffle(Deck.deck)
    
    def show_deck(self):
        print('Your deck has:')
        for card in Deck.deck:
            print(card)



class Chips():

    #TAKES IN YOUR BUDGET AND BET
       
    def __init__(self):
            pass


    def budget_and_bet(self):

        global budget, bet
        while True:
            try:
                print('\n')
                budget = int(input("What's your budget?  "))
                bet = int(input("What's your bet?  "))
            except:
                print("INVALID AMOUNT! Enter again")
                continue
            else:
                if bet > budget:
                    print("INVALID AMOUNT! Enter again")
                    continue
                else:
                    break    
        print('\n')
    


class CardDeal():

    def __init__(self):
        pass

    
    def deal_player(self):
    
        #RETURNS THE LAST CARD FROM DECK AND REMOVES IT FROM DECK
        player_hand.append(Deck.deck[-1])
        self.add_value(Deck.deck[-1].rank)
        self.check_for_ace(Deck.deck[-1])
        return Deck.deck.pop()

    def add_value(self, card):
    
        #TAKES IN RANK OF CARD AND RETURN NEW VALUE
        global value
        value += values[card]

    def check_for_ace(self, card):
    
        #CHECKS IF RANK IS ACE 
        if card == 'ace':
            if value > 21:
                value -= 10
            else:
                pass
        else:
            pass
     
    def deal_dealer(self):
    
        #RETURNS THE LAST CARD FROM DECK AND REMOVES IT FROM DECK
        dealer_hand.append(Deck.deck[-1])
        self.add_value_dealer(Deck.deck[-1].rank)
        self.check_for_ace_dealer(Deck.deck[-1])
        return Deck.deck.pop()

    def add_value_dealer(self, card):
    
        #TAKES IN RANK OF CARD AND RETURN NEW VALUE
        global dealervalue
        dealervalue += values[card]

    def check_for_ace_dealer(self, card):
    
        #CHECKS IF RANK IS ACE 
        if card == 'ace':
            if dealervalue > 21:
                dealervalue -= 10
            else:
                pass
        else:
            pass

    def hit_or_stand(self):

        #ASKS IF A PLAYER HITS OR TAKES STAND
        global status
        h_or_s = input("Would you like to hit or stand?  ")
        if h_or_s[0].lower() == 'h':
            status = True 
        else:
            status = False

    def check_for_bust(self, value):
        if value > 21:
            return True
        else:
            return False
   
    def show_hand(self):
        print("Dealer's hand:")
        print(dealer_hand[1])
        print('Hidden card')
        
        print('\n')

        print("Player's hand:")
        for card in player_hand:
            print(card)
        print(f"Total: {value}")
        print('\n')
    
def reset():

    global status
    choice = ' '
    while choice[0].lower() != 'y' and choice[0].lower() != 'n':
        choice = input("Do you want to play again?(Y/N)")
    if choice[0].lower() == 'y':
        status = True
    else:
        status = False




while True:

    #CREATE AND SHUFFLE A DECK
    mydeck = Deck()
    mydeck.create_deck()
    mydeck.shuffle_deck()

    #TAKE BUDGET AND BET 
    player_chips = Chips()
    player_chips.budget_and_bet()
    
    #START GAME PROVIDING 2 CARDS TO DEALER AND PLAYER
    card_deal = CardDeal()
    card_deal.deal_dealer()
    card_deal.deal_dealer()
    card_deal.deal_player()
    card_deal.deal_player()
    card_deal.show_hand()

    #NOW PLAYER PLAYS THE GAME UNTIL STANDS OR BUSTS
    while True:
        card_deal.hit_or_stand()
        if status == True:
            card_deal.deal_player()
            if card_deal.check_for_bust(value):
                card_deal.show_hand()
                print("BUST!!! You Lost")
                print('\n')
                break
            card_deal.show_hand()
            continue
        
        #RUNS WHEN PLAYER STANDS
        elif status == False:
            while dealervalue < value:
                card_deal.deal_dealer()
            if dealervalue > 21:
                print("Computer Busts!!! You won!")
                for card in dealer_hand:
                    print(card) 
                print(f"Total: {dealervalue}")
            else:
                print("Computer Won")
                for card in dealer_hand:
                    print(card)
                print(f"Total: {dealervalue}")
        break
    
    reset()
    if status == True:
        value = 0
        dealervalue = 0
        player_hand = []
        dealer_hand = []
        budget = 0
        bet = 0
        continue
    else:
        break
            






    

    

                
            
            





            
            



