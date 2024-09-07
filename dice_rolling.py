
import random

class DiceRoller:
    def __init__(self):
        self._sides = 6

    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, value):
        if value > 0:
            self._sides = value

    def roll(self):
        return random.randint(1, self._sides)
