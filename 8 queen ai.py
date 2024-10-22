
# Function to check if placing a queen at (row, col) is safe
def is_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the N-Queens problem using backtracking
def solve_nqueens(board, col):
    if col >= len(board):  # If all queens are placed
        return True

    # Try placing a queen in all rows one by one
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1  # Place queen
            
            # Recursively place the rest of the queens
            if solve_nqueens(board, col + 1):
                return True

            # If placing queen in row i doesn't lead to a solution, remove it
            board[i][col] = 0

    return False  # If no solution is found

# Function to print the board
def print_board(board):
    for row in board:
        print(" ".join('Q' if x == 1 else '.' for x in row))
    print()

# Function to initiate the 8-Queens problem
def solve_8queens():
    N = 8  # Number of queens
    board = [[0] * N for _ in range(N)]  # Create an 8x8 chess board

    if solve_nqueens(board, 0):  # Start solving from the first column
        print_board(board)  # Print the solution
    else:
        print("No solution found.")

# Solve the 8-Queens problem
solve_8queens()
