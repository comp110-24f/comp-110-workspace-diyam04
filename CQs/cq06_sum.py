"""Summing the elements of a list using different loops"""

__author__ = "730669985"

def w_sum(vals: list[float]) -> float:
    sum = 0.0
    index = 0
    
    while index < len(vals):
        sum += vals[index]
        index += 1
    
    return sum
#uses the local variable of sum to keep track of what has been added during the while loop

def f_sum(vals: list[float]) -> float:
    sum = 0.0
    
    for value in vals:
        sum += value
    
    return sum
#uses a sum local variable to keep track of the values added after a for loops goes through the list

def f_range_sum(vals: list[float]) -> float:
    sum = 0.0
    
    for index in range(len(vals)):
        element = vals[index]
        sum += element
    
    return sum
#uses the range function to iterate through the list using a for loop and egt the sum of the list
