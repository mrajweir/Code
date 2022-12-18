import MonopolyDeluxe
import unittest


class TestMonopolyDeluxe(unittest.TestCase):

    def test_doesRollDiceWork(self):
        for i in range(1, 1000):
            dice = MonopolyDeluxe.roll_dice()
            self.assertLess(dice, 7)
            self.assertGreater(dice, 0)