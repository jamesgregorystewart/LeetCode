""" Compute Pascal's Triangle

Write a program which given an integer n, will return the first n rows of pascal's triangle"""

"""
Idea:
    - b(n) = a(n-1)+a(n)

Time: O(n^2)
Space: O(n^2)

"""

from typing import List

def first_n_rows_of_pascals_triangle(n: int) -> List[List[int]]:
    triangle = []

    for i in range(1, n+1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
            else:
                row.append(triangle[i-2][j-1]+triangle[i-2][j])
        triangle.append(row)
    return triangle

print(first_n_rows_of_pascals_triangle(3))
print(first_n_rows_of_pascals_triangle(4))

print(first_n_rows_of_pascals_triangle(5))
