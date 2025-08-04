import random

# Word list with hints
words_with_hints = [
    ("elephant", "A large animal with a trunk"),
    ("python", "A popular programming language"),
    ("pizza", "A cheesy Italian dish"),
    ("guitar", "A musical instrument with strings"),
    ("mountain", "A large natural elevation of the earth's surface"),
    ("ocean", "A vast body of salt water"),
    ("computer", "An electronic device for processing data"),
    ("hangman", "A word guessing game"),
    ("chocolate", "A sweet treat made from cocoa"),
    ("astronaut", "A person trained to travel in space"),
    ("library", "A place where books are kept")
]

# Pick a random word and hint
word, hint = random.choice(words_with_hints)
word = word.lower()
guessed_letters = []
max_attempts = 10

# Function to show current progress
def display_progress():
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

print("Welcome to the Word Guessing Game!")
print("Hint:", hint)
print(f"You have {max_attempts} attempts. Good luck!")

# For loop controls the max attempts
for attempt in range(max_attempts):
    print("\nWord:", display_progress())
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single alphabet character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        remaining = max_attempts - (attempt + 1)
        print(f"Wrong guess! Attempts left: {remaining}")

else:
    print("\n Game Over! The correct word was:", word)
