"""Mutating functions"""

__author__ = "730669985"

def manual_append(list: list[int], value: int) -> None:
    "Add a value to the end of the list"
    list.append(value)

def double(original_list: list[int]) -> None:
    """Use a while loop to go double the numbers in the original list"""
    index = 0
    while index < len(original_list):
        original_list[index] *= 2
        index += 1

list_1: list[int] = [1,2,3]
list_2 = list_1
#Global variables that have the same list to begin with 

double(list_2)
#call to the double function to double the values within list 2

print(list_1)
print(list_2)
#print statements to print the values of list_1 and list_2 into the terminal



