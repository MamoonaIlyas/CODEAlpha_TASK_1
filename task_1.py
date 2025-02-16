import random  # Importing random module to choose a random word

# Function to select a random word from the list
def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge", "computer", "science"]
    return random.choice(words)

# Function to display the word with guessed letters revealed and others as underscores
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Main function to run the Hangman game
def hangman():
    word = choose_word()  # Selects a random word from the list
    guessed_letters = set()  # Stores the letters guessed by the player
    attempts = 6  # Maximum incorrect guesses allowed
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))  # Displays current progress of the word
        guess = input("Guess a letter: ").lower()  # Takes input from the user and converts it to lowercase
        
        # Validating input: Must be a single alphabetic character
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)  # Add guessed letter to the set
        
        if guess in word:
            print("Good guess!")  # If guess is correct
        else:
            attempts -= 1  # Reduce attempts for incorrect guess
            print(f"Wrong guess! Attempts left: {attempts}")
        
        # Check if the player has guessed all letters correctly
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return
    
    print("\nGame Over! The word was:", word)  # Display game over message if attempts run out

# Run the game if this script is executed directly
if __name__ == "__main__":
    hangman()
