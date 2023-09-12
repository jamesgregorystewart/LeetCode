""" Sudoku Validator """

"""
Idea:
    - iterate 0->80 with two nested for loops with range(9) each
    - Derive row, col, and square location from i and j
    - Maintain a set for each to check if sudoku board is valid


Time: O(1) Since there are a constant 81 iterations
Space: O(1) Since there are at most 81 elements to be stored
"""

from typing import List

def is_sudoku_valid(board: List[List[int]]) -> bool:
    for i in range(9):
        row, col, square = [], [], []
        sq_row_start, sq_col_start = (i // 3) * 3, (i % 3) * 3
        for j in range(9):
            sq_row, sq_col = sq_row_start + (j // 3), sq_col_start + (j % 3)
            if board[i][j] not in row and board[j][i] not in col and board[sq_row][sq_col] not in square:
                if board[i][j] == 0 pass else row.append(board[i][j])
                if board[j][i] == 0 pass else col.append(board[j][i])
                if board[sq_row][sq_col] == 0 pass else square.append(board[sq_row][sq_col])
            else return False
    return True
