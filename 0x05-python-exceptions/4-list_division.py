#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element of two lists.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the result list.

    Returns:
        list: A new list with element-wise divisions.

    """
    result = []
    try:
        for i in range(list_length):
            try:
                division = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                division = 0
                print("division by 0")
            except (TypeError, ValueError):
                division = 0
                print("wrong type")
            except IndexError:
                division = 0
                print("out of range")
            finally:
                result.append(division)
    finally:
        return result
