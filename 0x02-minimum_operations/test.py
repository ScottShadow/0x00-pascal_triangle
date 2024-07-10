#!/usr/bin/python3
import unittest
minOperations = __import__('0-minoperations').minOperations


class TestMinOperations(unittest.TestCase):
    def test_min_operations(self):
        self.assertEqual(minOperations(1), 0)  # No operations needed
        self.assertEqual(minOperations(4), 4)  # Copy, Paste, Paste, Paste
        # Copy, Paste, Copy, Paste, Paste
        self.assertEqual(minOperations(6), 5)
        # Copy, Paste, Paste, Copy, Paste, Paste
        self.assertEqual(minOperations(9), 6)
        # Copy, Paste, Paste, Paste, Copy, Paste, Paste, Paste
        self.assertEqual(minOperations(15), 8)


if __name__ == '__main__':
    unittest.main()
