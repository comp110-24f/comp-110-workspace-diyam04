"""Guessing game for guessing a secret number"""

__author__ = "730669985"

def guess_a_number() -> None:
    secret:int = 7
    guess:str = input("Guess a number: ")
    print ("Your guess was " + guess)
#You can assign a local variable to input by setting local variable equal to input and the string so I did for guess
    
    if int(guess) == secret: 
        print("You got it!")
    elif int(guess) < secret: 
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(guess) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
#There were three conditions so I used else if for the middle condition which was if they guessed a low number

if __name__ == "__main__":
   guess_a_number()