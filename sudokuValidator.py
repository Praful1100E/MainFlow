def is_valid_sudoku(board):
    def is_valid_unit(unit):
        """Check if a row, column, or 3x3 grid contains unique numbers (1-9)."""
        unit = [num for num in unit if num != 0]  # Remove zeros (empty spaces)
        return len(unit) == len(set(unit))  # Check for duplicates

    # Check rows
    for row in board:
        if not is_valid_unit(row):
            return False

    # Check columns
    for col in zip(*board):  # Transpose to get columns
        if not is_valid_unit(col):
            return False

    # Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(subgrid):
                return False

    return True

# Example usage
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
print(is_valid_sudoku(sudoku_board))