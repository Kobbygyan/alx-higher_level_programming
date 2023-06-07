#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(num1, num2, num3):
    """Match bytecode provided by Holberton School."""
    if num1 < num2:
        return num3
    if num3 > num2:
        return num1 + num2
