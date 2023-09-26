""" Search a 2D Matrix """

# You are given an m x n integer matrix matrix with the following two properties:
#
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
#
# You must write a solution in O(log(m * n)) time complexity.
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
#
# Constraints:
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

"""
Idea:
    - Consider 2D array as a 1D array
    - number of columns and mid are used to find the value, disregard columns in this computation
"""

from typing import List
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[mid//cols][mid%cols] == target:
                return True
            elif matrix[mid//cols][mid%cols] < target:
                l = mid + 1 
            else:
                r = mid - 1

        return False

solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 16))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 1))
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
print(solution.searchMatrix([[1],[3]], 3))

