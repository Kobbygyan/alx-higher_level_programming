#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import result_add, result_sub, result_mul, result_div

a = 10
b = 5

print("{} + {} = {}".format(a, b, result_add(a, b)))
print("{} - {} = {}".format(a, b, result_sub(a, b)))
print("{} * {} = {}".format(a, b, result_mul(a, b)))
print("{} / {} = {}".format(a, b, result_div(a, b)))
