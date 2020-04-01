import unittest
import utils
import classes
import sys
import io
from unittest import mock
from unittest.mock import patch


class TestFunctions(unittest.TestCase):
    def __int__(self):
        pass

    def setUp(self):
        self.deck = classes.Deck()
        self.deck.shuffle()
        self.players_hand = classes.Hand('player')
        self.dealers_hand = classes.Hand('dealer')
        self.players_hand.draw_card(self.deck.deal())
        self.players_hand.draw_card(self.deck.deal())
        utils.first_hand(self.players_hand, self.dealers_hand)
        utils.play_hand(self.deck, self.players_hand)
        utils.dealer_sim(self.deck, self.players_hand, self.dealers_hand)
        utils.reset_deck(self.players_hand, self.dealers_hand)



        self.card1 = classes.Card("\u2663", "7")
        self.card2 = classes.Card("\u2665", "J")
        self.card3 = classes.Card("\u2666", "3")
        self.card4 = classes.Card("\u2660", "5")
        self.card5 = classes.Card("\u2666", "A")
        self.card6 = classes.Card("\u2663", "Q")
        
        text_trap = io.StringIO()
        sys.stdout = text_trap
        

    def test_(self):
        with mock.patch("time.sleep"):
            self.assertEqual(utils.dealer_sim(21, 21), "You both hit 21! Push")
            self.assertEqual(utils.dealer_sim(18, 14), "Player wins with 18")
            self.assertEqual(utils.dealer_sim(13, 18), "Dealer wins with 18")
            self.assertEqual(utils.dealer_sim(40, 18), "You went bust, you lose")
            self.assertEqual(utils.dealer_sim(18, 18), "You both had the same score of 18 Push!")
            self.assertEqual(utils.dealer_sim(18, 22), "Dealer went bust! You win!")
            
    def test_dealer_sim(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        self.util
        self.assertEqual(utils.dealer_goes(21, "dealer"), "dealer")
        self.assertEqual(utils.dealer_goes(20, "dealer"), "dealer")
        self.assertEqual(utils.dealer_goes(22, "dealer"), None)


    def test_first_hand(self):
        hand = utils.first_hand(self.players_hand, self.dealers_hand)
        self.assertIsInstance(hand, list)
        self.assertIsInstance(hand.suit, str)
        self.assertIsInstance(hand.rank, str)
        self.assertIsInstance(hand.count, int)
        
    input_1 = "h"
    input_2 = "s"
    input_3 = "asd"

    @patch('builtins.input', return_value=input_1)
    def play_hand1(self, mock_input):
        self.assertEqual(utils.play_hand(), "h")

    @patch('builtins.input', return_value=input_2)
    def play_hand2(self, mock_input):
        self.assertEqual(utils.play_hand(), "s")

    def test_hit(self):
        with unittest.mock.patch("utils.play_hand", return_value="h"):
            with mock.patch("utils.") as pm_patch:
                utils.hit(self.deck, self.dealers_hand)
                self.assertTrue(pm_patch.called)

    @patch("utils.hitting")
    def test_player_moves(self, hitting_mock):
        self.assertEqual(utils.player_moves(self.players_hand), "Congrats your at 21, let\'s see what the dealer has!")
        utils.player_moves(self.dealers_hand)
        self.assertTrue(hitting_mock.called)

    def test_check_for_black_jack(self):
        self.assertEqual(utils.check_for_black_jack(self.players_hand, self.dealers_hand), False)
        self.assertEqual(utils.check_for_black_jack(self.dealers_hand, self.players_hand), False)
        self.assertEqual(utils.check_for_black_jack(self.dealers_hand, self.dealers_hand), True)

    def test_dealer_moves(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        with mock.patch("time.sleep"):
            self.assertEqual(utils.dealer_moves(self.players_hand, self.dealers_hand), 21)
            self.assertLess(self.dealers_hand.score, utils.dealer_moves(self.dealers_hand, self.players_hand))

        reset_deck(players_hand, dealers_hand)
        play_again()

class TestCards(unittest.TestCase):
    def __int__(self):
        pass

    def test_card_init(self):
        card = classes.Card(0, 0)
        assert isinstance(card, classes.Card)
        assert isinstance(card, object)


class test_Deck(unittest.TestCase):
    def __int__(self):
        pass

    def test__deck(self):
        deck = classes.Deck()
        self.assertIsInstance(self.deck, classes.Deck)
        self.assertIsInstance(self.deck, object)

    def test_deal(self):
        deck = classes.Deck()
        card1 = deck.deal()
        card2 = deck.deal()
        card3 = deck.deal()
        self.assertIsInstance(card1, classes.Card)
        self.assertIsInstance(card1, object)
        self.assertIsInstance(card2, classes.Card)
        self.assertIsInstance(card2, object)
        self.assertIsInstance(card3, classes.Card)
        self.assertIsInstance(card3, object)


class test_Hand()(unittest.TestCase):
    def __int__(self):
        pass

    def setUp(self):
        self.players_hand = classes.Hand()
        self.dealers_hand = classes.Hand()
        self.card1 = classes.Card("\u2663", "8")
        self.card2 = classes.Card("\u2665", "J")
        self.card3 = classes.Card("\u2666", "10")
        self.card4 = classes.Card("\u2660", "2")
        self.card5 = classes.Card("\u2666", "K")
        self.card6 = classes.Card("\u2663", "A")

    def test_hand(self):
        self.assertEqual(classes.Hand().hand(self.players_hand, (4, 5), (5, 6)), [(4, 5), (5, 6)])
        self.assertIsInstance(classes.Hand().hand(self.dealers_hand, self.card1, self.card2), list)

    def test_calc_score(self):
        self._player3.cards.append(self.card1)
        self._player3.cards.append(self.card2)
        self._player4.cards.append(self.card5)
        self._player4.cards.append(self.card6)
        self._player5.cards.append(self.card5)
        self._player5.cards.append(self.card6)
        self._player5.cards.append(self.card4)
        self.assertEqual(classes.Hand().calc_score(self._player3), 18)
        self.assertEqual(classes.Hand().calc_score(self._player4), 21)
        self.assertEqual(classes.Hand().calc_score(self._player5), 13)

    def test_hit(self):
        text_trap = io.StringIO()
        sys.stdout = text_trap
        self._player5.cards.append(self.card5)
        self._player5.cards.append(self.card6)
        self._player3.cards.append(self.card3)
        self._player3.cards.append(self.card2)
        self._player4.cards.append(self.card6)
        self._player5.cards.append(self.card4)
        self.assertEqual(classes.Hand().hit(self._player5, self.card1), 4)
        self.assertEqual(classes.Hand().hit(self._player3, self.card1), 3)
        self.assertEqual(classes.Hand().hit(self._player4, self.card1), 2)


if __name__ == '__main__':
    unittest.main()
