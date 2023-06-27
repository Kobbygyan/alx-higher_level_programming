#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Print an integer and handle potential errors.

    Args:
        value: The value to print.

    Returns:
        True if the value is an integer and printed successfully,
        False otherwise.

    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        return False
