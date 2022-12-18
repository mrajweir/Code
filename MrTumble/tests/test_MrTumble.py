import MrTumble
import unittest


class TestMrTumble(unittest.TestCase):

    def test_doesLuhnDetectValidNumbers(self):
        luhn_component = MrTumble.is_luhn_valid("400000000002")
        self.assertEqual(luhn_component, True)

    def test_doesLuhnDetectInvalidNumbers(self):
        luhn_component = MrTumble.is_luhn_valid("4000000000003")
        self.assertEqual(luhn_component, False)

    def test_canFindCard(self):
        # There has got to be a more elegant way to find if a value in a dictionary exists in a list - and I bet it
        # involves sets or better structuring the data too.
        output = MrTumble.find_card("400000", "0002")

        for d in output:
            if d["card_number"] == "40000000000002":
                self.assertEqual(True, True)
                return

        self.assertEqual(True, False)

    def test_cantFindCardIntentionally(self):
        # There has got to be a more elegant way to find if a value in a dictionary exists in a list - and I bet it
        # involves sets or better structuring the data too.
        output = MrTumble.find_card("400000", "0002")

        for d in output:
            if d["card_number"].__eq__("4000000000000003"):
                self.assertEqual(True, False)

        # Remember! It shouldn't be able to find that PAN in the output
        self.assertEqual(True, True)
