from random import randint

number_of_player = input("Please a enter a number between 2 and 6 for number of players : ")

cards_dealt = []


class Player:
    cards_in_hand = []
    player_number = 0


class Card:

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

    for i in range(1, int(number_of_player)):
        player = Player
        player.player_number = i
        players_made.append(player)

    return players_made


def deal_hands(players):
    for i in range(0, 5):
        for player in players:
            card_suit = randint(0, 3)
            card_number = randint(1, 14)
            card = Card(card_suit, card_number)
            player.cards_in_hand.append(card.number + card.suit)


def print_hands(players):
    for player in players:
        print("Player : %s" % player.player_number)
        for card in player.cards_in_hand:
            print(card)


print_hands(deal_hands(creating_players()))

