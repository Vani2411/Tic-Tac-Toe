import random


ROWS = "ABC"
COLS = "123"

def make_board():
   
   return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("  1   2   3")
    for i in range(3):
        row_display = ROWS[i] + " "
        for j in range(3):
            row_display += board[i][j]
            if j < 2:
                row_display += " | "
        print(row_display)
        if i < 2:
            print("  ---------")


# def check_winner(board, current_player):
#     if (board[0][0] == board[0][1] == board[0][2] != " ") or \
#        (board[1][0] == board[1][1] == board[1][2] != " ") or \
#        (board[2][0] == board[2][1] == board[2][2] != " ") or \
#        (board[0][0] == board[1][0] == board[2][0] != " ") or \
#        (board[0][1] == board[1][1] == board[2][1] != " ") or \
#        (board[0][2] == board[1][2] == board[2][2] != " ") or \
#        (board[0][0] == board[1][1] == board[2][2] != " ") or \
#        (board[0][2] == board[1][1] == board[2][0] != " "):
#         print(f"Player {current_player} wins!")
#         return True

def check_winner(board):
    """
    Return 'X' or 'O' if there is a winner, otherwise None.
    Checks the 8 winning lines (3 rows, 3 cols, 2 diagonals).
    """
    lines = []

    # Rows
    lines.extend(board)

    # Columns
    for c in range(3):
        lines.append([board[0][c], board[1][c], board[2][c]])

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    # If any line is all same non-space symbol, that's the winner
    for line in lines:
        if line[0] != " " and line[0] == line[1] == line[2]:
            return line[0]

    return None

def is_draw(board):
    """Draw if no empty cells left and no winner."""
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    """Return list of empty positions."""
    cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                cells.append((r, c))
    return cells

def user_move(board, player):
    while True:
       
        user_input = input(f"Enter your move player {player} (ex. A1, B2, C1) : ").strip()
        if user_input.lower() == "exit":
            print("Thanks for playing! Goodbye!")
            break
        move = user_input.upper()

        if len(move) != 2 or move[0] not in ROWS or move[1] not in COLS:
            print("invalid move!!! Try again.")
            continue
        row = ROWS.index(move[0])
        col = COLS.index(move[1])
        
        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue
        
        board[row][col] = player
        return True


def show_help():
    print(
        "\nHow to play:\n"
        "- Enter moves like A1, B2, C3\n"
        "- Rows are A, B, C and columns are 1, 2, 3\n"
        "- Type 'exit' during a game to return to the menu\n"
        "- Win by getting 3 in a row (horizontal, vertical, diagonal)\n"
    )

def choose_game_mode():
    while True:
        mode = input("Choose game mode:\n1. Single Player (vs Computer)\n2. Two Player\nEnter 1 or 2: ")
        if mode in ["1", "2"]:
            return mode
        else:
            print("❌ Invalid choice. Please enter 1 or 2.\n")

def single_player():
    board = make_board()
    print("\nSingle Player Mode (You = X, AI = O)")
    print("Type 'exit' to return to menu.\n")
    print_board(board)

    while True:
        if not user_move(board, "X"):
            return
        print_board(board)

         #check for winner
        winner = check_winner(board)
        if winner == 'X':
            print(f"\n🏁 {winner} wins!")
            return

        # Check for draw
        if is_draw(board):
            print("\n🤝 It's a draw!")
            return

        r, c = random.choice(get_empty_cells(board))
        board[r][c] = "O"

        print(f"\nAI plays: {ROWS[r]}{COLS[c]}")
        print_board(board)

        if check_winner(board) == "O":
            print("\n🏁 AI wins!")
            return

        if is_draw(board):
            print("\n🤝 It's a draw!")
            return


def two_player():
    board = make_board()
    current_player = "X"

    print("\nMultiplayer Mode (Player X vs Player O)")
    print("Type 'exit' to return to menu.\n")
    print_board(board)

    while True:
        if not user_move(board, current_player):
            return

        print()
        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"\n🏁 Player {winner} wins!")
            return

        if is_draw(board):
            print("\n🤝 It's a draw!")
            return
        
        current_player = "O" if current_player == "X" else "X"



def menu():
    while True:
        print("===== Tic-Tac-Toe =====")
        print("1. Play Game")
        print("2. Help")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            mode = choose_game_mode()
            if mode == "1":
                single_player()
            else:
                two_player()

        elif choice == "2":
            show_help()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")



if __name__ == "__main__":
    menu()
