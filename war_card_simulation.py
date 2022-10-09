"""
The classic card game: War

The game will be a simulation of 2 computer players, playing eachother
in a game of war.
"""

import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Jack", "Queen", "King", "Ace"
    )
card_values = {
    'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
    'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12,
    'King': 13,  'Ace': 14
    }

# Number of Cards required to be placed for war
war_draw = 3


# CARD CLASS
# SUIT, RANK, VALUE
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = card_values[rank]

    def __str__(self) -> str:
        return self.rank + " of " + self.suit


# DECK CLASS
class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle_deck(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


# PLAYER CLASS
class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.cards_in_play = []
        self.played_cards = []

    def play_one(self):
        if len(self.hand) == 0:
            random.shuffle(self.played_cards)
            self.hand.extend(self.played_cards)
            self.played_cards = []

        self.cards_in_play.append(self.hand.pop(0))
        self.current_card = self.cards_in_play[-1]

    def add_cards(self, new_cards):
        if isinstance(new_cards, list):
            self.played_cards.extend(new_cards)
        else:
            self.played_cards.append(new_cards)

    def reset_cards_in_play(self):
        self.cards_in_play = []

    def __str__(self):
        return f"Player {self.name} has {len(self.hand)} cards."


def reset_all_cards_in_play():
    for i in [player_one, player_two]:
        i.reset_cards_in_play()


# GAME LOGIC

# GAME SETUP
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle_deck()


while len(new_deck.all_cards) > 0:
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True

round_num = 0

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.hand) == 0 and len(player_one.played_cards) == 0:
        print("Player One, out of cards! Player Two Wins!")
        game_on = False
        break

    if len(player_two.hand) == 0 and len(player_two.played_cards) == 0:
        print("Player Two, out of cards! Player One Wins!")
        game_on = False
        break

    # START A NEW ROUND
    reset_all_cards_in_play()

    player_one.play_one()
    player_two.play_one()

    at_war = True

    while at_war:

        if player_one.current_card.value > player_two.current_card.value:
            player_one.add_cards(player_one.cards_in_play)
            player_one.add_cards(player_two.cards_in_play)
            at_war = False
            break

        elif player_two.current_card.value > player_one.current_card.value:
            player_two.add_cards(player_one.cards_in_play)
            player_two.add_cards(player_two.cards_in_play)
            at_war = False
            break

        else:
            print("WAR!")
            print(player_one.current_card, player_two.current_card)

            if {
                len(player_one.hand) < war_draw
                and len(player_one.hand) < war_draw
            }:
                for num in range(len(player_one.hand)):
                    player_one.play_one()

                for num in range(len(player_two.hand)):
                    player_two.play_one()

            elif len(player_one.hand) < war_draw:
                for i in range(len(player_one.hand)):
                    player_one.play_one()

                for num in range(war_draw):
                    player_two.play_one()

            elif len(player_two.hand) < war_draw:
                for i in range(len(player_two.hand)):
                    player_two.play_one()

                for num in range(war_draw):
                    player_one.play_one()

            else:
                for num in range(war_draw):
                    player_one.play_one()
                    player_two.play_one()
