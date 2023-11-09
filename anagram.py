def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    count = 0
    
    for letter in first_string:
        if letter in second_string:
            count +=1

    if count == len(first_string):
        return True
    else:
        return False
    


