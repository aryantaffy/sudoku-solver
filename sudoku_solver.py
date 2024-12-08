# Sudoku Solver Program
def is_valid(board, row, col, num):
    """Check if placing `num` at board[row][col] is valid."""
    # Check the row
    if num in board[row]:
        return False
    # Check the column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Try numbers 1-9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number
                        if solve_sudoku(board):  # Recursively solve
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # No valid number found, backtrack
    return True  # Solved

def print_board(board):
    """Print the Sudoku board in a readable format."""
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

if __name__ == "__main__":
    # Example Sudoku Puzzle (use 0 for empty cells)
    puzzle = [
        [6, 0, 3, 0, 0, 0, 0, 0, 0],
        [1, 9, 0, 5, 7, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 4, 8, 0, 0, 6, 0, 0, 3],
        [3, 0, 0, 0, 2, 0, 0, 0, 6],
        [9, 0, 0, 3, 0, 0, 8, 4, 0],
        [0, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 2, 0, 6, 1],
        [0, 0, 0, 0, 0, 0, 7, 0, 2],
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle)

    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:")
        print_board(puzzle)
    else:
        print("\nNo solution exists for this puzzle.")
