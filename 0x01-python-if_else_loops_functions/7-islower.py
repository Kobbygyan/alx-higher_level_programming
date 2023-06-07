#!/usr/bin/python3
# 7-islower.py

def islower(char):
    """Check for lowercase characters."""
    if ord(char) >= 97 and ord(char) <= 122:
        return True
    else:
        return False
