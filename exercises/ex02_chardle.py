"""EX02 - Chardle - A cute step toward Wordle."""
 
__author__ = "730669985"

def input_word() -> str:
    """"Returns the word from the user"""
    word_from_user:str = input("Enter a 5-character word: ")
#Word is a string and defined by input of user
    if len(word_from_user) == 5: 
        print (word_from_user)
        return word_from_user
#if was used to return the word if it contained 5 letters and then I used else to print the error statement
    else:
        print("Error: Word must contain 5 characters.") 
        exit()
#Exit is outside of the else because I found that the number of characters was not 5 and needed to exit

def input_letter() -> str:
    """"Returns the letter from the user"""
    letter_from_user: str = input ("Enter a single character: ")
#letter_from_user is a string defined by input from user
    if len(letter_from_user) == 1:
        print(letter_from_user)
        return letter_from_user
#I used if to give return the letter from user if it was one character and else to return the error statement
#I could have used if len(letter_from_user) =! 5 but I like == more cause it just makes more sense to me
    else: 
        print ("Error: Character must be a single character.")
        exit()
#I placed exit outside of the else cause I needed to exit after I found the characters to be more than 1

def contains_char(word:str, letter:str) -> None:
    """Checks the number of matching characters"""
    instances_of_letter:int = 0
    index:int = 0
#instances_of_letter was needed as a local variable to count how many times a letter showed up
    print("Searching for " + letter + " in " + word)
    
    while index < len(word):
        if word[index] == letter:
            instances_of_letter+= 1
            print(letter + " found at index " + str(index))
        index += 1
#while loop looks through the word entered and finds the number of the letter the user inputs
    if instances_of_letter == 0:
        print("No instances of " + letter + " found in " + word)
    elif instances_of_letter == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(instances_of_letter) +" instances of " + letter + " found in " + word)
#three possible types of scenarios were possible where the letter they guess is not there, where one letter is there, or when there is more than one letter there
#three conditions can be contained in if, elif, and else

def main() -> None:
    word:str = input_word()
    letter:str = input_letter()
    contains_char(word, letter)
#word and letter need to be defined as strings because they return strings

if __name__ == "__main__":
    main()