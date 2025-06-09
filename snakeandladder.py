# snake and ladder game using file handling in python.

import random

snakes = {17: 7, 54: 34, 62: 19, 98: 79}
ladders = {3: 38, 24: 33, 42: 93, 72: 84}

position = 0

# Open log file
log_file = open("game_log.txt", "w")

print("Snake and Ladder Game!")
print("Reach 100 to win.\n")
log_file.write("Game Started\n")

while position < 100:
    try:
        input("Press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print("You rolled:", dice)
        log_file.write(f"Dice rolled: {dice}\n")

        if position + dice <= 100:
            position += dice

        if position in snakes:
            print("Oops! Snake at", position)
            log_file.write(f"Snake at {position} -> {snakes[position]}\n")
            position = snakes[position]

        elif position in ladders:
            print("Yay! Ladder at", position)
            log_file.write(f"Ladder at {position} -> {ladders[position]}\n")
            position = ladders[position]

        print("Current position:", position, "\n")
        log_file.write(f"Current position: {position}\n\n")

    except:
        print("Something went wrong. Try again.")
        log_file.write("Exception occurred.\n")

print("Congratulations! You won!")
log_file.write("Player reached 100. Game Won!\n")
log_file.close()
