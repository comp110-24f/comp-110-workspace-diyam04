"""Practice with conditionals"""


def less_than_10(num:int) -> None:
    """Tell me if num < 10 """
    if num < 10:
        print("Small number")
    else:
        print("Big number!")
    print("Have a nice day!")
    
    
def should_i_eat(hungry:bool) -> None:
    """Tells me whether or not to eat based on hunger"""
    if hungry:
        print("Eat some food silly goose!")
    else: 
        print("Do your Comp 110 homework instead") #else block
    print("i'm proud of you <3") #either way be kind to yourself

should_i_eat(hungry=True)

def check_first_letter(word:str, letter:str)-> str:
    "Give me back match if the first character of the word is a letter"
    if word[0] == letter: 
        return "match!"
    else:
        return "no match!"

 