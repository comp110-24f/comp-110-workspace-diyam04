"""Plannning a tea party for guests with tea bags and treats"""
#I briefly forgot that I needed to name the exercise at the beginning, so then I went back and added a docstring explaining the purpose of the exercise

__author__: str = "730669985"

def main_planner(guests:int) -> None:
    """Be the entrypoint to my program"""
    # Added str(guests) to signify the guests at the party
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # Since tea_bags usually returns an int, I needed to convert the int into a string before adding to print
    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Inside of each function call if there is a parameter, you need to include a parameter in code while printing so I did for both tea bags and treats
    print("Treats: " + str(treats(people=guests)))
    # Cost has two different parameters, tea bags and treats, so both needed to be included in the print statement
    print("Cost: $" + str(cost(tea_bags(people=guests),treats(people=guests))))
    # People has to equal guests because the parameters for tea bags and treats are not guests they are people
    

def tea_bags(people:int) -> int:
    """Return the number of tea bags needed for people attending the tea party"""
    return people * 2
# Multiplied the number of tea bags by 2 to get the number of tea bags needed for the function


def treats(people: int) -> int:
    """ Returns the number of treats needed for each guest given that they each drink two teas and need 1.5 treats per tea they drink"""
    # It took me a while to remember that the return function can return anything including function calls multiplied by number
    return int(tea_bags(people=people) * 1.5)
# Called the tea bag function and multiplied by 1.5 to determine the number of treats needed for tea party


def cost(tea_count:int, treat_count:int) -> float:
    """Returns the cost of tea bags and treats"""
    # Used float after return to ensure a float was returned for the total cost
    return float(tea_count*0.50 + treat_count * 0.75)

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
