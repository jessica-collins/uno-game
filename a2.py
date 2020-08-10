#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Jessica Collins 44345956"


class Card(object):
    """
    A card represents a card in the uno game which has colour and number attributes
    """
    def __init__(self, number, colour):
        """Creates a card with a number and colour

        Parameters:
            number(int): The number attribute of the card
            colour(str): The colour attribute of the card
        """
        self._number = number
        self._colour = colour

    def get_number(self):
        """(int) Returns the number attribute of the card"""
        return self._number

    def get_colour(self):
        """(str) Returns the colour attribute of the card"""
        return self._colour

    def set_number(self, number):
        """Sets the new number attribute of the card

        Parameters:
            number(int): The new number
        """
        self._number = number

    def set_colour(self, colour):
        """Sets the new colour attribute of the card

        Parameters:
            colour(str): The new colour
        """
        self._colour = colour

    def get_pickup_amount(self):
        """(int) Returns the amount of cards the next player should pick up"""
        return 0

    def matches(self, card):
        """Returns whether or not the next card to be placed on the pile matches the current cards

        Parameters:
            card: The current card
        """
        if self._colour == card.get_colour():
            match = True

        elif self._number == card.get_number():
            match = True

        else:
            match = False
        return match

    def play(self, player, game):
        """Performs a special card action"""
        return None

    def __str__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "Card({0}, {1})".format(self._number, self._colour)

    def __repr__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "Card({0}, {1})".format(self._number, self._colour)


class SkipCard(Card):
    """A skip card represents a card in the uno game which has a colour attribute and skips the turn of the next
    player"""
    def __init__(self, number, colour):
        """Creates a skip card with a number and colour

        Parameters:
            number(int): The number attribute of the card
            colour(str): The colour attribute of the card
        """
        super().__init__(number, colour)

    def play(self, player, game):
        """Performs a special card action - skips the next player in the game"""
        self._player = Player(player)
        return game.skip()

    def __str__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "SkipCard({0}, {1})".format(self._number, self._colour)

    def __repr__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "SkipCard({0}, {1})".format(self._number, self._colour)


class ReverseCard(Card):
    """A reverse card represents a card in the uno game which has a colour attribute and reverses the order of turns"""
    def __init__(self, number, colour):
        """Creates a reverse card with a number and colour

        Parameters:
            number(int): The number attribute of the card
            colour(str): The colour attribute of the card
        """
        super().__init__(number, colour)

    def play(self, player, game):
        """Performs a special card action - reverses the order of turns in the game"""
        self._player = Player(player)
        return game.reverse()

    def __str__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "ReverseCard({0}, {1})".format(self._number, self._colour)

    def __repr__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "ReverseCard({0}, {1})".format(self._number, self._colour)


class Pickup2Card(Card):
    """A pick up 2 card represents a card in the uno game which has a colour attribute and makes the next player pick
    up 2 cards"""
    def __init__(self, number, colour):
        """Creates a pickup 2 card with a number and colour

        Parameters:
            number(int): The number attribute of the card
            colour(str): The colour attribute of the card
        """
        super().__init__(number, colour)

    def get_pickup_amount(self):
        """(int) Returns the amount of cards the next player should pick up"""
        return 2

    def play(self, player, game):
        """Performs a special card action - reverses the order of turns in the game"""
        self._player = Player(player)
        next_player = game._turns.peak()
        next_player_deck = next_player.get_deck()
        drawn_cards = game.pickup_pile.pick(amount=2)
        next_player_deck = next_player_deck.get_cards().extend(drawn_cards)
        return next_player_deck

    def __str__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "Pickup2Card({0}, {1})".format(self._number, self._colour)

    def __repr__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "Pickup2Card({0}, {1})".format(self._number, self._colour)


class Pickup4Card(Card):
    """A pick up 4 card represents a card in the uno game which has a colour attribute and makes the next player pick
    up 4 cards"""
    def __init__(self, number, colour):
        """Creates a pickup 4 card with a number and colour

        Parameters:
            number(int): The number attribute of the card
            colour(str): The colour attribute of the card
        """
        super().__init__(number, colour)

    def get_pickup_amount(self):
        """(int) Returns the amount of cards the next player should pick up"""
        return 4

    def matches(self, card):
        """Returns whether or not the next card to be placed on the pile matches the current cards

        Parameters:
            card: The current card
        """
        return True

    def play(self, player, game):
        """Performs a special card action - reverses the order of turns in the game"""
        self._player = Player(player)
        next_player = game._turns.peak()
        next_player_deck = next_player.get_deck()
        drawn_cards = game.pickup_pile.pick(amount=4)
        next_player_deck = next_player_deck.get_cards().extend(drawn_cards)
        return next_player_deck

    def __str__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "Pickup4Card({0}, {1})".format(self._number, self._colour)

    def __repr__(self):
        """(str) Returns a textual representation of the card as Card(number, colour)"""
        return "Pickup4Card({0}, {1})".format(self._number, self._colour)


class Deck(object):
    """A deck represents a collection of ordered Uno cards belonging to a player"""
    def __init__(self, starting_cards = None):
        """Creates a deck of cards for a player

        Parameters:
            starting_cards: The starting deck for the player
        """
        if starting_cards == None:
            self.starting_cards = []
        else:
            self.starting_cards = starting_cards

    def get_cards(self):
        """(list) Returns the cards in the deck"""
        return self.starting_cards

    def get_amount(self):
        """(int) Returns the amount of cards in the deck"""
        return len(self.starting_cards)

    def shuffle(self):
        """(list) Returns the cards in the deck in a randomised order"""
        random.shuffle(self.starting_cards)

    def pick(self, amount=1):
        """(list) Returns the first 'amount' of cards

        Parameters:
             amount (int): The amount of cards to be returned
        """
        removed_cards = self.starting_cards[-1 * amount:]
        del self.starting_cards[-1 * amount:]
        return removed_cards

    def add_card(self, card):
        """(list) Adds a card on top of the deck"""
        self.starting_cards.append(card)

    def add_cards(self, cards):
        """(list) Adds a list of cards on top of the deck"""
        self.starting_cards.extend(cards)

    def top(self):
        """(str) Returns the card on top of the deck, or None if the deck is empty"""
        if len(self.starting_cards) == 0:
            return None
        else:
            return self.starting_cards[-1]


class Player:
    """A player represents one of the players in the game of Uno"""
    def __init__(self, name):
        """Creates a player with a name

        Parameters:
            name(str): The name of the player
        """
        self._name = name
        self._deck = Deck([])

    def get_name(self):
        """(str) Returns the name of the player"""
        return self._name

    def get_deck(self):
        """(list) Returns the cards in the player's deck"""
        return self._deck

    def is_playable(self):
        """Returns whether or not the player's moves are automatic"""
        raise NotImplementedError

    def has_won(self):
        """Returns whether or not the player has an empty deck and has therefore won"""
        if self._deck.get_amount() == 0:
            return True
        else:
            return False

    def pick_card(self, putdown_pile):
        """Selects a card to play from the player's deck"""
        raise NotImplementedError


class HumanPlayer(Player):
    """A human player represents one of the players in the game of Uno that selects cards to play using the GUI"""
    def __init__(self, name):
        """Creates a human player with a name

        Parameters:
            name(str): The name chosen for the human player
        """
        super().__init__(name)

    def is_playable(self):
        """Returns whether or not the player's moves are automatic"""
        return True

    def pick_card(self, putdown_pile):
        """Selects a card to play from the player's deck"""
        return None

class ComputerPlayer(Player):
    """A computer player represents one of the players in the game of Uno that selects cards to play automatically"""
    def __init__(self, name):
        """Creates a computer/automated player with a name

        Parameters:
            name(str): The name chosen for the computer player
         """
        super().__init__(name)

    def is_playable(self):
        """Returns whether or not the player's moves are automatic"""
        return False

    def pick_card(self, putdown_pile):
        """Selects a card to play from the player's deck"""
        top_card = putdown_pile.get_cards()[-1]
        for element in self._deck.get_cards():
            if element.matches(top_card):
                putdown_pile.get_cards().append(element)
                return element
        return None

def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()
