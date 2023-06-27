#!/usr/bin/python3

def raise_exception_msg(message=""):
    """Raise a name exception with a custom message.

    Args:
        message (str): The custom message for the exception.

    Raises:
        NameError: Always raises a name exception with the provided message.

    """
    raise NameError(message)
