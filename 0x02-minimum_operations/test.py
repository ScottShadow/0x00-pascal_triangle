#!/usr/bin/python3
import unittest
minOperations = __import__('0-minoperations').minOperations


class TestMinOperations(unittest.TestCase):
    def test_min_operations(self):
        self.assertEqual(minOperations(1), 0)  # No operations needed
        self.assertEqual(minOperations(0), 0)
        self.assertEqual(minOperations(-5), 0)
        self.assertEqual(minOperations(2), 2)
        self.assertEqual(minOperations(4), 4)  # Copy, Paste, Paste, Paste
        # Copy, Paste, Copy, Paste, Paste
        self.assertEqual(minOperations(6), 5)
        # Copy, Paste, Paste, Copy, Paste, Paste
        self.assertEqual(minOperations(9), 6)
        # Copy, Paste, Paste, Paste, Copy, Paste, Paste, Paste
        self.assertEqual(minOperations(15), 8)

    def test_min_operations_wrong_type(self):
        self.assertRaises(TypeError, minOperations, "n")
        self.assertRaises(TypeError, minOperations, None)

        self.assertRaises(TypeError, minOperations, 1.5)
        self.assertRaises(TypeError, minOperations, [1, 2, 3])
        self.assertRaises(TypeError, minOperations, {1: "a", 2: "b"})


if __name__ == '__main__':
    unittest.main()
