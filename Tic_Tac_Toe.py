import math

# Define the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # Top row
        [board[1][0], board[1][1], board[1][2]],  # Middle row
        [board[2][0], board[2][1], board[2][2]],  # Bottom row
        [board[0][0], board[1][0], board[2][0]],  # Left column
        [board[0][1], board[1][1], board[2][1]],  # Center column
        [board[0][2], board[1][2], board[2][2]],  # Right column
        [board[0][0], board[1][1], board[2][2]],  # Diagonal top-left to bottom-right
        [board[2][0], board[1][1], board[0][2]]   # Diagonal bottom-left to top-right
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'X'):
        return 10 - depth
    elif check_winner(board, 'O'):
        return depth - 10
    elif is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column): ").split())
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    break
                else:
                    print("Cell is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid move. Please enter row and column as two integers (0, 1, or 2).")

        if check_winner(board, 'O'):
            print_board(board)
            print("Congratulations! You win!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # AI move
        print("AI is making a move...")
        row, col = best_move(board)
        board[row][col] = 'X'

        if check_winner(board, 'X'):
            print_board(board)
            print("AI wins! Better luck next time.")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        print_board(board)

if __name__ == "__main__":
    main()
