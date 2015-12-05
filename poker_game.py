from random import randint

number_of_player = input("Please a enter a number between 2 and 6 for number of players : ")

cards_dealt = []


class Player:
    def __int__(self, player_number):
        self.player_number = player_number
        self.cards_in_hand = []


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


def creating_player_number():
    players_made = []

    for i in range(1, int(number_of_player)):
        players_made.append(Player(i))

    return players_made

card = Card(3, 13)
print(card.suit)
print(card.number)







"""
def deal_hands(players):
    for i in range(0, 1):
        for player in players:
            card_number = str(randint(1, 14))
            if card_number == "11":

                card_number = "J"
                player.cards_in_hand.append(card_number)

            elif card_number == "12":

                card_number = "Q"
                player.cards_in_hand.append(card_number)

            elif card_number == "13":

                card_number = "K"
                player.cards_in_hand.append(card_number)

            elif card_number == "14":

                card_number = "A"
                player.cards_in_hand.append(card_number)

            else:
                player.cards_in_hand.append(card_number)

"""