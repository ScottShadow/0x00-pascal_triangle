#!/usr/bin/python3
import unittest
validUTF8 = __import__('0-validate_utf8').validUTF8


class TestValidUTF8(unittest.TestCase):

    def test_valid_utf8(self):
        # Test a valid UTF-8 encoding
        data = [65, 108, 105, 110, 103, 116, 104, 101, 114]
        self.assertTrue(validUTF8(data))

    def test_invalid_utf8(self):
        # Test an invalid UTF-8 encoding
        data = [229, 65, 127, 256]
        self.assertFalse(validUTF8(data))

    def test_empty_data(self):
        # Test an empty data set
        data = []
        self.assertTrue(validUTF8(data))

    def test_single_byte_utf8(self):
        # Test a single byte UTF-8 encoding
        data = [65]
        self.assertTrue(validUTF8(data))

    def test_two_byte_utf8(self):
        # Test a two byte UTF-8 encoding
        data = [0xc3, 0xa9]
        self.assertTrue(validUTF8(data))

    def test_three_byte_utf8(self):
        # Test a three byte UTF-8 encoding
        data = [0xe0, 0xa4, 0xb9]
        self.assertTrue(validUTF8(data))

    def test_four_byte_utf8(self):
        # Test a four byte UTF-8 encoding
        data = [0xf0, 0x90, 0x8d, 0x88]
        self.assertTrue(validUTF8(data))

    def test_invalid_two_byte_utf8(self):
        # Test an invalid two byte UTF-8 encoding
        data = [0xc0, 0xaf]
        self.assertFalse(validUTF8(data))

    def test_invalid_three_byte_utf8(self):
        # Test an invalid three byte UTF-8 encoding
        data = [0xe0, 0x80, 0xc0]
        self.assertFalse(validUTF8(data))

    def test_invalid_four_byte_utf8(self):
        # Test an invalid four byte UTF-8 encoding
        data = [0xf8, 0x80, 0x80, 0x80]
        self.assertFalse(validUTF8(data))


if __name__ == '__main__':
    unittest.main()
