#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    num_arguments = len(argv)

    print("Number of argument(s):", end=" ")
    if num_arguments == 0:
        print(".", end="")
    else:
        print(num_arguments, end=" ")
        if num_arguments == 1:
            print("argument:")
        else:
            print("arguments:")

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))
