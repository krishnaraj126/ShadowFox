import random

# List of words
words = ["python", "apple", "table", "guitar"]

# Pick a random word
word = random.choice(words)

# Initialize guessed letters and lives
guessed_letters = []
lives = 7

print("Welcome to Hangman!")

# Main game loop
while lives > 0:
    # Show current progress
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print("\nWord:", display)
    
    # Check if player won
    if "_" not in display:
        print("You won! The word was:", word)
        break
    
    # Ask for input
    guess = input("Enter a letter to guess: ").lower()
    
    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue  # Skip rest of loop, ask again
    
    # Add guess to guessed letters
    guessed_letters.append(guess)
    
    # Wrong guess
    if guess not in word:
        lives -= 1
        print("Wrong! Lives left:", lives)
    
    # Check if player lost
    if lives == 0:
        print("You lost! The word was:", word)
        break
