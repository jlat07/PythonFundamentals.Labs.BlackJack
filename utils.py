import time
from classes import *

'''
Functions needed for Black Jack Game

'''

playing = True
def blackjack(name: Hand):
    '''
    Tells the player that the dealer has won
    '''
    print(f'{name.name} has black Jack')
    print(f'{name.name} Wins')
    playing = False
    return playing

def bust(name: Hand):
    '''
    If dealer or player goes over 21, this bust function shows the had and lets player know a bust has occured
    '''
    time.sleep(1)
    print(f"BUST! {name.name} loses")
    playing = False
    return playing
    
def dealer_sim(deck: Deck, player: Hand, dealer: Hand):
    '''
    After player has made all choices, this function runs through the dealers scenerios and deciedes when to hit or Stands
    also, deciedes who wins and calls the corresponding function
    '''
    if player.count > 21:
        bust(player)
        return
    else:
        print("Dealer turn's")
        time.sleep(1)
        show_hand(dealer)
        time.sleep(2)
        while dealer.count <= 17:
            print('Dealer Hits:')
            time.sleep(1)
            hit(deck, dealer)
            show_hand(dealer)
            time.sleep(1)
        if dealer.count > 21:
            bust(dealer)
        elif dealer.count == 21:
            blackjack(dealer)
        elif dealer.count > 17:
            if dealer.count > player.count:
                time.sleep(1)
                print('Dealer Stands:')
                time.sleep(1)
                show_hand(player)
                time.sleep(1)
                winner(dealer)
            if dealer.count < player.count:
                if player.count == 21:
                    blackjack(player)
                else:
                    print('Dealer Stands:')
                    time.sleep(1)
                    winner(player)
            elif dealer.count == player.count:
                push(dealer)

def first_hand(player: Hand, dealer: Hand):
    '''
    Shows the first hand with one dealer card not turned over
    '''
    print(f"{dealer.name}'s hand")
    print(f'[], {dealer.cards[1]}')
    time.sleep(2)
    print('\n')
    print(f"{player.cards[0]} {player.cards[1]} {player.count}")
    print(f"{player.name}'s hand")

def hit(deck: Deck, name: Hand):
    '''
    Function draws a card from the deck and addes it to the hand. While taking in consnameeration of an ace, and
    if user bust on the hit, it will call the bust function
    '''
    hit = deck.deal()
    name.draw_card(hit)
    name.ace()
    if name.count > 21:
        return

def play_again():
    '''
    Starts the game over, or lets user quit
    '''
    if input('Would you like to play again? (y/n): ') == 'y':
        playing = False
        return playing
    else:
        print("         \                           /")
        print("          \                         /")
        print("           \  Thanks For Playing   /")
        print("            ]                     [    ,'|")
        print("            ]                     [   /  |")
        print("            ]___               ___[ ,'   |")
        print("            ]  ]\             /[  [ |:   |")
        print("            ]  ] \           / [  [ |:   |")
        print("            ]  ]  ]         [  [  [ |:   |")
        print("            ]  ]  ]__     __[  [  [ |:   |")
        print("            ]  ]  ] ]\ _ /[ [  [  [ |:   |")
        print("           ]  ]  ] ] (#) [ [  [  [ :==== '")
        print("           ]  ]  ]_].nHn.[_[  [  [")
        print("           ]  ]  ]  HHHHH. [  [  [")
        print('           ]  ] /   `HH("N  \ [  [')
        print("           ]__]/     HHH  '  \[__[")
        print("           ]         NNN         [")
        print("           ]         N/'         [")
        print("           ]         N H         [")
        print("          /          N            \ ")
        print("         /           q,            \ ")
        print("        /                           \ ")
        quit()

def play_hand(deck: Deck, name: Hand):
    '''
    This is where the player deciedes to hit or stay
    '''
    while name.count <= 21:
        I = input("h: to Hit or s: to Stand: ")
        if I == 'h':
            hit(deck, name)
            time.sleep(1)
            show_hand(name)
        if I == 's':
            print("Player Stands")
            break

def winner(name):
    '''
    Lets the platey know that the player has won
    '''
    show_hand(name)
    time.sleep(1)
    print(f'{name.name} Wins')
    playing = False
    return playing

def push(name):
    '''
    Calls the out come of the game, when dealer and player have the same count, push is invoked
    '''
    show_hand(name)
    print('Push, No Winner!')
    playing = False
    return playing

def show_hand(name: Hand):
    '''
    Function shows the hand specific to the instance of the paramater its given
    '''
    H = [card for card in name.cards]
    print(f"{name.name}'s hand:{H}{name.count}")

def reset_deck(player: Hand, dealer: Hand):
    player.cards = []
    dealer.cards = []