from random import randint
import math

number_of_player = input("Please a enter a number between 2 and 6 for number of players : ")

cards_dealt = []


class Player:
    def __init__(self, player_number):
        self.cards_in_hand = []
        self.player_number = player_number


class Card:
    cards_dealt = []

    def set_suit(self, number_for_suit):
        suit = ""
        if number_for_suit == 0:
            suit = "♠"

        elif number_for_suit == 1:
            suit = "♥"

        elif number_for_suit == 2:
            suit = "♦"

        elif number_for_suit == 3:
            suit = "♣"
        return suit

    def set_number(self, number_on_card):
        # I don't know what's going on here but i will find out later
        card_number = ""
        if number_on_card == 11:
            card_number = "J"

        elif number_on_card == 12:
            card_number = "Q"

        elif number_on_card == 13:
            card_number = "K"

        elif number_on_card == 14:
            card_number = "A"
        else:
            card_number = str(number_on_card)

        return card_number

    def __init__(self, number_for_suit, number_on_card):
        self.suit = self.set_suit(number_for_suit)
        self.number = self.set_number(number_on_card)


def creating_players():
    players_made = []

    for i in range(1, int(number_of_player) + 1):
        players_made.append(Player(i))

    return players_made


def is_dealt(cards_in_list, target_item):
    in_list = False
    if target_item in cards_in_list:
        in_list = True
        return in_list


def deal_hands(players):
    for i in range(0, 5):
        for player in players:
            card_suit = randint(0, 3)
            card_number = randint(1, 14)
            card = Card(card_suit, card_number)
            while is_dealt(cards_dealt, str(card.number)+str(card_suit)):
                card_suit = randint(0, 3)
                card_number = randint(1, 14)
                card = Card(card_suit, card_number)
                break
            player.cards_in_hand.append(card.number + card.suit)
            cards_dealt.append(str(card.number)+str(card_suit))
    return players


def print_hands(players):
    for player in players:
        print()
        print("Player : %s" % player.player_number)
        for card in player.cards_in_hand:
            print(card + " ", end="")
        print()


print_hands(deal_hands(creating_players()))
