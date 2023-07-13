#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    # Create a new list to store the modified elements
    result = []

    # Iterate over the elements in the input list
    for item in my_list:
        # If the element matches the search value, replace it with the new value
        if item == search:
            result.append(replace)
        else:
            result.append(item)

    return result
