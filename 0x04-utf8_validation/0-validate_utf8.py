#!/usr/bin/python3
"""
    UTF-8 Validation
"""


def validUTF8(data):
    """ Validate UTF-8 Encodings """
    num_bytes = 0
    for num in data:
        num = format(num, '#010b')[-8:]

        # start of new char
        if num_bytes == 0:
            num_bytes = get_byte_count(num)-1
            if num_bytes is None:
                return False

        elif num.startswith("10"):
            num_bytes -= 1

        else:
            return False
    return num_bytes == 0


def get_byte_count(num):
    """ Get byte count of character """
    prefix_dict = {
        "0": 1,
        "110": 2,
        "1110": 3,
        "11110": 4,
        }

    return next(
        (
            value
            for prefix, value in prefix_dict.items()
            if num.startswith(prefix)
        ),
        False,
    )