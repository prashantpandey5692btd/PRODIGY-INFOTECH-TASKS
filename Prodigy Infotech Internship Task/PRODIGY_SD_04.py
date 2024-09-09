# Function to check if it's valid to place a number in a specific cell
def is_valid(board, row, col, num):
    # Check if the number is already in the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check if the number is already in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number is already in the 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    # Find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try placing numbers 1-9 in the empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        # Place the number
                        board[row][col] = num

                        # Recursively try to solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If placing num doesn't lead to a solution, backtrack
                        board[row][col] = 0

                # If no number works, return False to trigger backtracking
                return False

    # If no empty cell is found, the puzzle is solved
    return True

# Function to print the Sudoku grid
def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            if col == 8:
                print(board[row][col])
            else:
                print(board[row][col], end=" ")

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku Puzzle: \n")
print_board(sudoku_board)

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Puzzle: \n")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
