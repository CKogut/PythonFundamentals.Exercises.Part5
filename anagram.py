def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    count = 0

    #check that they are the same length
    if len(first_string) != len(second_string):
      return False
    
    for letter in first_string:
        if letter in first_string:
            count +=1

    if count == len(first_string):
        return True
    


