import random

# List of possible words for the game
words_list = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'react']

# Function to display the word with underscores for unguessed letters
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Main function to play the game
def hangman():
    word = random.choice(words_list)  # Select a random word from the list
    guessed_letters = []  # List to keep track of guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Limit for incorrect guesses

    print("Welcome to Hangman!")
    
    # Game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        # Ask player for a guess
        guess = input("Guess a letter: ").lower()
        
        # Validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You've already guessed the letter '{guess}'. Try a different one.")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1
        
        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()