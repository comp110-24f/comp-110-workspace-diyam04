__author__ = "730669985"


def num_instances(phrase:str, search_char:str)-> int:
    """Return the count of occurences in search_char in phrase"""
    count:int = 0 
    index:int = 0 

    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1 
        index += 1 
    return count

num_instances("should", "l")



