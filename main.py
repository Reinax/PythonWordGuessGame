# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pathlib
import random

WORDLIST = pathlib.Path("wordlist.txt")
words = [
    word.upper()
    for word in WORDLIST.read_text(encoding="utf=8").strip().split("\n")
]

word = random.choice(words)

for guess_num in range(1,7):
    guess = input(f"\nGuess {guess_num}: ").upper()
    if guess == word:
        print("Correct")
        break
    correct_letters = {
        letter for letter, correct in zip(guess, word) if letter == correct
    }
    misplaced_letters = set(guess) & set(word) - correct_letters
    wrong_letters = set(guess) - set(word)

    print("correct letters:", ", ".join(sorted(correct_letters)))
    print("misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("wrong letters:", ", ".join(sorted(wrong_letters)))
else:
    print(f"Unlucky... The word was {word}")
