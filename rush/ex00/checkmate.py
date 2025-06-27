#!/usr/bin/env python3
def checkmate(board_str):
    lines = board_str.strip().split('\n')
    size = len(lines)

    # ตรวจสอบว่าทุกแถวมีความยาวเท่ากับขนาดกระดาน
    for row in lines:
        if len(row) != size:
            print("Fail")  # กระดานไม่ใช่สี่เหลี่ยมจัตุรัส
            return

    # สร้างกระดาน
    board = [list(row) for row in lines]
    king_count = 0
    king_x, king_y = -1, -1

    # ตรวจหาตำแหน่งของ King และตัวอักษรผิด
    for y in range(size):
        for x in range(size):
            cell = board[y][x]
            if cell == 'K':
                king_count += 1
                king_x, king_y = x, y
            elif cell not in ['.', 'R', 'B', 'Q', 'P']:
                print("Fail")  # ตัวอักษรไม่ถูกต้อง
                return

    if king_count != 1:
        print("Fail")  # ต้องมี King เพียงตัวเดียว
        return
################################  ATTACKING LINE  #####################################################################
    
    # ตรวจสอบแนวตรง: Rook หรือ Queen
    straight_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in straight_directions:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < size and 0 <= y < size:
            piece = board[y][x]
            if piece == 'R' or piece == 'Q':
                print("Success")
                return
            if piece != '.':
                break
            x += dx
            y += dy

    # ตรวจสอบแนวทแยง: Bishop หรือ Queen
    diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in diagonal_directions:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < size and 0 <= y < size:
            piece = board[y][x]
            if piece == 'B' or piece == 'Q':
                print("Success")
                return
            if piece != '.':
                break
            x += dx
            y += dy

    # ตรวจสอบ Pawn (สมมุติว่าโจมตีจากด้านล่างไปบน)
    for dx in [-1, 1]:
        x, y = king_x + dx, king_y + 1
        if 0 <= x < size and 0 <= y < size:
            if board[y][x] == 'P':
                print("Success")
                return

    print("Fail")
