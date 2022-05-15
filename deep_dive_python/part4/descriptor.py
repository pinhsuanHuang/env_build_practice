from datetime import datetime
from random import choice, seed


class TimeUTC:
    def __get__(self, instance, owner_class):
        return datetime.utcnow().isoformat()


class Logger:
    time = TimeUTC()


class Choice:
    def __init__(self, *choices):
        self._choices = choices

    def __get__(self, instance, owner_class):
        return choice(self._choices)


class Deck:
    suit = Choice('Spade', 'Heart', 'Diamond', 'Club')
    card = Choice(*'23456789JQKA', '10')


class Dice:
    dice = Choice(1, 2, 3, 4, 5, 6)


if __name__ == '__main__':
    l = Logger()
    print(l.time)
    deck = Deck()
    print(deck.suit, deck.card)
    dice = Dice()
    print(dice.dice)
