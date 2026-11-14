import random

# List of words
words = ["python", "computer", "program", "engineer", "keyboard"]

# Random word selection
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=" * 35)
print("🎮 Welcome to Hangman Game 🎮")
print("=" * 35)
print("Guess the word one letter at a time!")

while wrong_guesses < max_wrong:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n🧩 Word:", display_word)
    print("🔤 Guessed letters:", guessed_letters)
    print("❤️ Attempts left:", max_wrong - wrong_guesses)

    # Win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("\n✍️ Guess a letter: ").lower()

    # Condition: Only letters allowed
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please type ONE letter only (no numbers or symbols).")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct / Wrong guess
    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")
    else:
        print("✅ Correct guess!")

# Lose condition
if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("📖 The word was:", word)

print("\n👋 Thanks for playing Hangman!")