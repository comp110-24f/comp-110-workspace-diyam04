"""Basic syntax of lists."""

#Create an empty list
my_numbers: list[float] = [] #literal
my_numbers:list[float] 

print(my_numbers)

#string analogy
#my name: str = "'" #literal
#my_name: str = str() #constructor

#Adding a value to it
my_numbers.append(1.5)
my_numbers.append(2)

#New List
game_points: list[int] =[102,86,94]
print (game_points)

#Subscription notation
print (game_points[2])
last_game:int = game_points[2]
print(last_game)

#Modifying by Index
game_points[1] = 72
print (game_points)

#Getting the length
len(game_points)

#Removing an Item
game_points.pop(1)
print (game_points)

#Function name: display
#Parameters: list of integers
#RV:None
#Print every element in the input list
#Call display on game points

def display (int_list:list(int))-> None:
    """Displays all elements of int_list"""

    index:int = 0

    while index < len(int_list):
        print(int_list:[index])
        index

