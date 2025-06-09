# tic_tac_toe_file.py

def initialize_board():
    return [" " for _ in range(9)]

def display_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def log_to_file(board, move, player):
    with open("tic_tac_toe.txt", "a") as file:
        file.write(f"Player {player} moved to position {move+1}\n")
        file.write("Current board:\n")
        file.write(f"{board[0]} | {board[1]} | {board[2]}\n")
        file.write("--+---+--\n")
        file.write(f"{board[3]} | {board[4]} | {board[5]}\n")
        file.write("--+---+--\n")
        file.write(f"{board[6]} | {board[7]} | {board[8]}\n\n")

def check_winner(board, player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw(board):
    return " " not in board

def play_game():
    board = initialize_board()
    current_player = "X"
    
    # Clear previous game log
    open("game_log.txt", "w").close()
    
    while True:
        display_board(board)
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = current_player
                log_to_file(board, move, current_player)

                if check_winner(board, current_player):
                    display_board(board)
                    print(f"🎉 Player {current_player} wins!")
                    with open("game_log.txt", "a") as file:
                        file.write(f"Player {current_player} wins!\n")
                    break
                elif is_draw(board):
                    display_board(board)
                    print("It's a draw!")
                    with open("game_log.txt", "a") as file:
                        file.write("The game is a draw!\n")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number from 1 to 9.")

if __name__ == "__main__":
    play_game()

