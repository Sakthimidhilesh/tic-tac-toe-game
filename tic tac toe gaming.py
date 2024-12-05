# Tic Tac Toe Game in Python

# Function to print the game board
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to check for a win
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def is_draw(board):
    return all(cell != " " for cell in board)

# Main game function
def play_game():
    # Initialize the board
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    
    while True:
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != " " or move < 0 or move > 8:
                print("Invalid move. Try again.")
                continue
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")
            continue
        
        # Make the move
        board[move] = current_player
        print_board(board)
        
        # Check for a winner
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        
        # Check for a draw
        if is_draw(board):
            print("It's a draw!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
