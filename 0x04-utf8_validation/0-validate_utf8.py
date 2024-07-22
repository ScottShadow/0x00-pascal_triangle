#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data: list) -> bool:
    """
    Returns True if data is a valid UTF-8 encoding, else return False
        Args:
            data (bool): a list of integers

        Returns:
            bool: True if data is a valid UTF-8 encoding, else return False
    """
    n_bytes = 0
    for byte in data:
        counter_mask = 1 << 7
        if not n_bytes:
            while byte & counter_mask:
                n_bytes += 1
                counter_mask >>= 1
            if not n_bytes:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
            # Overlong encoding check
            # 2-byte character must be at least 0b11000010 (C2 in hex)
            if n_bytes == 2 and byte < 0b11000010:
                return False
            # 3-byte character must be at least 0b11100000 (E0 in hex)
            if n_bytes == 3 and byte < 0b11100000:
                return False
            # 4-byte character must be at least 0b11110000 (F0 in hex)
            if n_bytes == 4 and byte < 0b11110000:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
        n_bytes -= 1
    return n_bytes == 0
