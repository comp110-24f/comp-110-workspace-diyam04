"""Testing how well I know list functions"""

__author__ ="730669985"

def all(int_list, num):
    """Return True if all integers in int_list are the same as num, False otherwise."""
    if len(int_list) == 0:  # sees if the list is empty
        return False
    
    for item in int_list:
        if item != num: 
            return False
            
    return True

def max(int_list: list[int]) -> int:
    """Returns the largest value in the list"""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    largest = int_list[0]  #starts off with the first element as the largest element
    for item in int_list:
        if item > largest:
            largest = item  # changes largest if the other elements are larger

    return largest #gives the largest value to the user

def is_equal(int_list1, int_list2):
    """Return True if every element at every index is equal in both lists""" 

    if len(int_list1) != len(int_list2): #checks if the lists are the same length
        return False
    
    for idx in range(len(int_list1)):
        if int_list1[idx] != int_list2[idx]: #checks if the values at each index are not the same
            return False

        else:
            return True    
    
def extend(int_list1,int_list2):
    """Mutates the first integer list by adding the elements of the second integer list to it"""
    for element in int_list2:
        int_list1.append(element) #adds on the elements in integer list 2 to integer list 1


