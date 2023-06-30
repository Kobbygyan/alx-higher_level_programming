#!/usr/bin/python3
def print_list_integer(custom_list=[]):
    """Prints all integers of a list"""
    for index in range(len(custom_list)):
        print('{:d}'.format(custom_list[index]))
