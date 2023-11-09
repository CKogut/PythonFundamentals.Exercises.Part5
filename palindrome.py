def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """

    # Remove any whitespace and convert to lower case
    value = value.replace(" ","")
    value = value.lower()

    # Reverse the string 
    valueR = value[::-1]

    # Compare the two values
    if value == valueR:
        return True
    else:
        return False
