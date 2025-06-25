from checkmate import is_check

def main():
    # Example 1: King is in check (Pawn)
    board1 = """\
........
Q..K....
."""
    print("Success" if is_check(board1) else "Fail")

    # Example 2: King is safe
    board2 = """\
..
.K"""
    print("Success" if is_check(board2) else "Fail")

if __name__ == "__main__":
    main()