def has_won(list_grid):
    # Check Cols
    if list_grid[0] == "X" and list_grid[1] == "X" and list_grid[2] == "X" or \
            list_grid[0] == "O" and list_grid[1] == "O" and list_grid[2] == "O":
        return True
    elif list_grid[3] == "X" and list_grid[4] == "X" and list_grid[5] == "X" or \
            list_grid[3] == "O" and list_grid[4] == "O" and list_grid[5] == "O":
        return True
    elif list_grid[6] == "X" and list_grid[7] == "X" and list_grid[8] == "X" or \
            list_grid[6] == "O" and list_grid[7] == "O" and list_grid[8] == "O":
        return True

    # Check Rows
    elif list_grid[6] == "X" and list_grid[3] == "X" and list_grid[0] == "X":
        return True
    elif list_grid[6] == "O" and list_grid[3] == "O" and list_grid[0] == "O":
        return True
    elif list_grid[7] == "X" and list_grid[4] == "X" and list_grid[1] == "X":
        return True
    elif list_grid[7] == "O" and list_grid[4] == "O" and list_grid[1] == "O":
        return True
    elif list_grid[8] == "X" and list_grid[5] == "X" and list_grid[2] == "X" or \
            list_grid[8] == "O" and list_grid[5] == "O" and list_grid[2] == "O":
        return True

    # Check Diag
    elif list_grid[0] == "X" and list_grid[4] == "X" and list_grid[8] == "X" or \
            list_grid[0] == "O" and list_grid[4] == "O" and list_grid[8] == "O":
        return True
    elif list_grid[2] == "X" and list_grid[4] == "X" and list_grid[6] == "X" or \
            list_grid[2] == "O" and list_grid[4] == "O" and list_grid[6] == "O":
        return True

    else:
        return None
