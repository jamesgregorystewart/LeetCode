""" Rotate 2D Array

Rotate a matrix 90 degrees clockwise"""

"""
Idea:
    - 

Trick:
    - Understanding the bitwise NOT operator would be useful to find the next index since it will negate then subtract 1 from the integer value.
"""

from typing import List

def rotate_matrix(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix) - 1
    for i in range(len(matrix)//2):
        for j in range(i, n - i):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]

    return matrix


print(rotate_matrix([[0,1],[3,2]]))
print(rotate_matrix([[0,1,2],[3,4,5],[6,7,8]]))
print(rotate_matrix([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]))
