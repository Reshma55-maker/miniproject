import random

try:
    word = random.choice(open("words.txt").read().split())
except:
    print("File not found!")
    exit()

guesses = []
tries = 6

while tries > 0:
    output = [c if c in guesses else '_' for c in word]
    print("Word:", ' '.join(output))

    if '_' not in output:
        print("You won!")
        open("result.txt", "a").write(f"WON - {word}\n")
        break

    guess = input("Guess: ").lower()
    if guess in guesses:
        print("Already guessed.")
        continue

    guesses.append(guess)
    if guess not in word:
        tries -= 1
        print("Wrong! Tries left:", tries)
else:
    print("You lost! Word was:", word)
    open("result.txt", "a").write(f"LOST - {word}\n")
