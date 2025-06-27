#!/usr/bin/env python3
from checkmate import checkmate

def main():
    # Test case from the example
    board = """
......
......
...K..
..Q...
......
......
"""
 
    checkmate(board)

if __name__ == "__main__":
    main()