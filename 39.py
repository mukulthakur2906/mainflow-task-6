def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == ".":
                continue
            if num in rows[r] or num in cols[c] or num in boxes[(r // 3) * 3 + c // 3]:
                return False
            rows[r].add(num)
            cols[c].add(num)
            boxes[(r // 3) * 3 + c // 3].add(num)
    return True

if __name__ == "__main__":
    print("Enter Sudoku board row by row (9 elements each, use '.' for empty):")
    board = [input(f"Row {i+1}: ").split() for i in range(9)]
    print("Valid Sudoku" if is_valid_sudoku(board) else "Invalid Sudoku")
