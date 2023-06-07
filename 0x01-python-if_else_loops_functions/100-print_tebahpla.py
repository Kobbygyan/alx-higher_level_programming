#!/usr/bin/python3
# 100-print_tebahpla.py

""""Print the alphabet in reverse order alternating upper- and lower-case."""
increment = 0
for char_code in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char_code - increment)), end="")
    increment = 32 if increment == 0 else 0
