from random import randint


number_of_player = input("Please a enter a number between 2 and 6 for number of players : ")


class Player:
    cards_in_hand = []

    def __int__(self, player_number):
        self.player_number = player_number


def creating_player_number():
    players_made = []

    for i in range(1, number_of_player-1):
        players_made.append(Player(i))

    return players_made


def deal_hands(players):

 for i in range(0, 1):
    for player in players:
        card_to_deal = str(randint(1, 14))
        if card_to_deal == "11":

            card_to_deal = "J"
            player.cards_in_hand.append(card_to_deal)

        elif card_to_deal == "12":

            card_to_deal = "Q"
            player.cards_in_hand.append(card_to_deal)

        elif card_to_deal == "13":

            card_to_deal = "K"
            player.cards_in_hand.append(card_to_deal)

        elif card_to_deal == "14":

            card_to_deal = "A"
            player.cards_in_hand.append(card_to_deal)

        else:
            player.cards_in_hand.append(card_to_deal)











