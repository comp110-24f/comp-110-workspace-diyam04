""""A fun little word game designed to replicate Wordle"""

__author__ = "730669985"

def input_guess(mystery_word_length: int) -> str:
    while True:
        user_input = input(f"Enter a {mystery_word_length} character word: ")
        if len(user_input) == mystery_word_length:
            return user_input
        else:
            print(f"That wasn't {mystery_word_length} chars! Try again:")
#Makes sure the user gives a guess that meets the word length of the mystery word

def contains_char(word: str, letter: str) -> bool:
    """Check if a certain letter is in a word and return True if it is and False if it's not"""
    assert len(letter) == 1, "letter must be a single character"

    for char in word:
        if char == letter:
            return True
    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Return a string of green emojis if there is a character in the right place, yellow emojis if the character is present but not in the right place, and then white if there is no character."""
    
    assert len(guess_word) == len(secret_word), "Guess and secret must be of the same length."

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    #These are the color codes for the three different boxes colors
    
    emoji_result: str = ""
    idx: int = 0
    
    # Make sure the green boxes are in the right place
    while idx < len(guess_word):
        if guess_word[idx] == secret_word[idx]:
            emoji_result += GREEN_BOX
        else:
            # Check if character is in the secret word
            if contains_char(secret_word, guess_word[idx]):
                emoji_result += YELLOW_BOX
            else:
                emoji_result += WHITE_BOX
        idx += 1
        
    return emoji_result

def main(secret_word: str) -> None:
    """The entrypoint of the program and main game loop."""
    
    MAX_TURNS = 6
    attempts = 0
    has_won = False
    # In Wordle each player has 6 turns to guess the word.
    while attempts < MAX_TURNS and not has_won:
        print(f"=== Turn {attempts + 1}/{MAX_TURNS} ===")
        
        # Get user's guess of the correct length
        player_guess = input_guess(mystery_word_length=len(secret_word))
        
        # Use emojis to check the guess
        result_emojis = emojified(player_guess, secret_word)
        print(result_emojis)

        # Check if the user has gotten the word
        if player_guess == secret_word:
            has_won = True
        attempts += 1

    # Game attempts messages
    if has_won:
        print(f"You won in {attempts}/{MAX_TURNS} turns!") 
        # gives the number of attempts the user won the game in
    else:
        print(f"X/{MAX_TURNS} - Sorry, try again tomorrow!")
        #gives this message if the user never gets the correct word

if __name__ == "__main__":
    main(secret_word="codes")
#this is a call to the main function that allows the program to execute

