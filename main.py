from utils import *


def main():
    '''
    Starts Game
    '''

    playing = True
    print("Welcome to JLAT's Python Black Jack")
    while playing:
        time.sleep(2)
        print("Shuffling Deck..")
        time.sleep(2)
        deck = Deck()
        deck.shuffle()
        print('Dealing Cards..')
        time.sleep(2)
        players_hand = Hand('player')
        dealers_hand = Hand('dealer')
        players_hand.draw_card(deck.deal())
        players_hand.draw_card(deck.deal())
        dealers_hand.draw_card(deck.deal())
        dealers_hand.draw_card(deck.deal())
        first_hand(players_hand, dealers_hand)
        time.sleep(1)
        play_hand(deck, players_hand)
        time.sleep(1)
        dealer_sim(deck, players_hand, dealers_hand)
        reset_deck(players_hand, dealers_hand)
        play_again()


if __name__ == '__main__':
    main()
