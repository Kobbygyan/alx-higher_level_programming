#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(string, index):
    """Create a copy of the string without the character at position n."""
    if index < 0:
        return string
    return string[:index] + string[index+1:]
