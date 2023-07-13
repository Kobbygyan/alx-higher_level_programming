#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of elements present in only one set."""
    # Create an empty set to store the unique elements
    unique_set = set()

    # Iterate over the elements in set_1
    for element in set_1:
        # Check if the element is not present in set_2
        if element not in set_2:
            # Add the element to the unique_set
            unique_set.add(element)

    # Iterate over the elements in set_2
    for element in set_2:
        # Check if the element is not present in set_1
        if element not in set_1:
            # Add the element to the unique_set
            unique_set.add(element)

    return unique_set
