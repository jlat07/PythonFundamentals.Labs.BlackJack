import time
from classes import Deck, Hand


'''
Functions needed for Black Jack Game
in alphabetical order (except end_game() which is at the end.)

'''
playing = True


def blackjack(name: Hand):
    '''
    Lets user know who has Black Jack
    '''
    print(f'{name.name} has black Jack')
    print(f'{name.name} Wins')


def bust(name: Hand):
    '''
    Lets user know who hast bust
    '''
    time.sleep(1)
    print(f"BUST! {name.name} loses")


def dealer_sim(deck: Deck, player: Hand, dealer: Hand):
    '''
    After player has made all choices, this function determines if player has blackjack or bust
    Or runs through the dealers scenerios and deciedes when to hit or Stand. Then returns outcome.
    '''
    if player.count == 21:
        return blackjack(player)
    if player.count > 21:
        return bust(player)
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
    Shows the first hand with one dealer card not turned over. Evaluates if player has 21
    '''
    print(f"{dealer.name}'s hand")
    print(f'[], {dealer.cards[1]}')
    time.sleep(2)
    print('\n')
    print(f"{player.cards[0]} {player.cards[1]} {player.count}")
    print(f"{player.name}'s hand")
    if player.count == 21:
        blackjack(player)


def hit(deck: Deck, name: Hand):
    '''
    Function draws a card from the deck and addes it to the hand.
    and the ace difference is taken into consideration.
    '''
    hit = deck.deal()
    name.draw_card(hit)


def play_again():
    '''
    Starts the game over, or lets user end game.
    '''
    i = input('Would you like to play again? (y/n): ')
    if i == 'y':
        return
    elif i == 'n':
        end_game()
    else:
        print('Invalid input')
        play_again()


def play_hand(deck: Deck, name: Hand):
    '''
    This is where the player deciedes to hit or stay
    '''
    while name.count <= 21:
        I = input("h: to Hit or s: to Stand: ")
        I = I.lower()
        if I == 'h':
            hit(deck, name)
            time.sleep(1)
            show_hand(name)
        elif I == 's':
            print("Player Stands")
            break
        else:
            print('Invalid input')


def winner(name):
    '''
    Lets the platey know that the player has won
    '''
    show_hand(name)
    time.sleep(1)
    print(f'{name.name} Wins')


def push(name):
    '''
    Calls the out come of the game, when dealer and player have the same count, push is invoked
    '''
    show_hand(name)
    print('Push, No Winner!')


def show_hand(name: Hand):
    '''
    Function shows the hand specific to the instance of the paramater its given
    '''
    H = [card for card in name.cards]
    print(f"{name.name}'s hand:{H}{name.count}")


def reset_deck(player: Hand, dealer: Hand):
    player.cards = []
    dealer.cards = []


def end_game():
    print("         \                           /")
    time.sleep(.1)
    print("          \                         /")
    time.sleep(.1)
    print("           \  Thanks For Playing   /")
    time.sleep(.1)
    print("            ]                     [    ,'|")
    time.sleep(.1)
    print("            ]                     [   /  |")
    time.sleep(.1)
    print("            ]___               ___[ ,'   |")
    time.sleep(.1)
    print("            ]  ]\             /[  [ |:   |")
    time.sleep(.1)
    print("            ]  ] \           / [  [ |:   |")
    time.sleep(.1)
    print("            ]  ]  ]         [  [  [ |:   |")
    time.sleep(.1)
    print("            ]  ]  ]__     __[  [  [ |:   |")
    time.sleep(.1)
    print("            ]  ]  ] ]\ _ /[ [  [  [ |:   |")
    time.sleep(.1)
    print("           ]  ]  ] ] (#) [ [  [  [ :==== '")
    time.sleep(.1)
    print("           ]  ]  ]_].nHn.[_[  [  [")
    time.sleep(.1)
    print("           ]  ]  ]  HHHHH. [  [  [")
    time.sleep(.1)
    print('           ]  ] /   `HH("N  \ [  [')
    time.sleep(.1)
    print("           ]__]/     HHH  '  \[__[")
    time.sleep(.1)
    print("           ]         NNN         [")
    time.sleep(.1)
    print("           ]         N/'         [")
    time.sleep(.1)
    print("           ]         N H         [")
    time.sleep(.1)
    print("          /          N            \ ")
    time.sleep(.1)
    print("         /           q,            \ ")
    time.sleep(.1)
    print("        /                           \ ")
    time.sleep(.1)
    quit()
