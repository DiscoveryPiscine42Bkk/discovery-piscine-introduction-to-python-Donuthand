def is_valid_board(board):
    """Check if the board is valid (square, one King, correct characters)."""
    if not board:
        return False
    rows = board.split('\n')
    size = len(rows)
    king_count = 0

    for row in rows:
        if len(row) != size:
            return False  # Not a square
        for char in row:
            if char not in 'KPRQB.':
                return False  # Invalid character
            if char == 'K':
                king_count += 1

    return king_count == 1  # Must have exactly one King

def locate_king(board):
    """Return the (row, col) position of the King."""
    rows = board.split('\n')
    for i, row in enumerate(rows):
        if 'K' in row:
            return (i, row.index('K'))
    return (-1, -1)  # Should not happen if board is valid

def is_check(board):
    """Check if the King is in check."""
    if not is_valid_board(board):
        return False  # Invalid board (handle as per requirements)

    king_row, king_col = locate_king(board)
    rows = board.split('\n')
    size = len(rows)

    # Check threats from each piece
    for i in range(size):
        for j in range(size):
            piece = rows[i][j]
            if piece == 'P':  # Pawn
                if (i == king_row + 1 and (j == king_col - 1 or j == king_col + 1)):
                    return True
            elif piece == 'B':  # Bishop
                if abs(i - king_row) == abs(j - king_col):
                    # Check if path is clear
                    step_row = 1 if i < king_row else -1
                    step_col = 1 if j < king_col else -1
                    r, c = i + step_row, j + step_col
                    while r != king_row and c != king_col:
                        if rows[r][c] != '.':
                            break  # Path blocked
                        r += step_row
                        c += step_col
                    else:
                        return True
            elif piece == 'R':  # Rook
                if i == king_row or j == king_col:
                    # Check if path is clear
                    if i == king_row:
                        step = 1 if j < king_col else -1
                        c = j + step
                        while c != king_col:
                            if rows[i][c] != '.':
                                break
                            c += step
                        else:
                            return True
                    else:  # j == king_col
                        step = 1 if i < king_row else -1
                        r = i + step
                        while r != king_row:
                            if rows[r][j] != '.':
                                break
                            r += step
                        else:
                            return True
            elif piece == 'Q':  # Queen (Bishop + Rook)
                if (abs(i - king_row) == abs(j - king_col)) or (i == king_row or j == king_col):
                    # Same logic as Bishop or Rook
                    if abs(i - king_row) == abs(j - king_col):  # Diagonal
                        step_row = 1 if i < king_row else -1
                        step_col = 1 if j < king_col else -1
                        r, c = i + step_row, j + step_col
                        while r != king_row and c != king_col:
                            if rows[r][c] != '.':
                                break
                            r += step_row
                            c += step_col
                        else:
                            return True
                    else:  # Straight
                        if i == king_row:
                            step = 1 if j < king_col else -1
                            c = j + step
                            while c != king_col:
                                if rows[i][c] != '.':
                                    break
                                c += step
                            else:
                                return True
                        else:  # j == king_col
                            step = 1 if i < king_row else -1
                            r = i + step
                            while r != king_row:
                                if rows[r][j] != '.':
                                    break
                                r += step
                            else:
                                return True
    return False