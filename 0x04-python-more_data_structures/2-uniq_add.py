#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list, only once for each integer."""
    # Create a set to store unique integers
    unique_set = set()

    # Iterate over the elements in the input list
    for element in my_list:
        # Check if the element is an integer
        if isinstance(element, int):
            # Add the integer to the set
            unique_set.add(element)

    # Calculate the sum of the unique integers in the set
    result = sum(unique_set)

    return result
