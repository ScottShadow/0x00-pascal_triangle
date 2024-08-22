import unittest

makeChange = __import__('0-making_change').makeChange


class TestMakeChangeFunction(unittest.TestCase):

    def test_valid_coins_and_total(self):
        coins = [1, 2, 5]
        total = 7
        self.assertEqual(makeChange(coins, total), 2)

    def test_invalid_coins_empty_list(self):
        coins = []
        total = 5
        self.assertEqual(makeChange(coins, total), -1)

    def test_invalid_total_negative_number(self):
        coins = [1, 2, 5]
        total = -3
        self.assertEqual(makeChange(coins, total), 0)

    def test_total_cannot_be_made_with_given_coins(self):
        coins = [2, 4]
        total = 3
        self.assertEqual(makeChange(coins, total), -1)

    def test_total_can_be_made_with_given_coins(self):
        coins = [1, 2, 5]
        total = 10
        self.assertEqual(makeChange(coins, total), 2)

    def test_total_given_with_negative_coins(self):
        coins = [-3, -6]
        total = 10
        self.assertEqual(makeChange(coins, total), -1)


if __name__ == '__main__':
    unittest.main()
