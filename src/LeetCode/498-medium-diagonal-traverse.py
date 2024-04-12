from typing import List
from collections import deque


# O(N) / O(N)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        ans = [deque() for _ in range(n + m - 1)]

        for r in range(n):
            for c in range(m):
                if (r + c) % 2:
                    ans[r + c].append(mat[r][c])
                else:
                    ans[r + c].appendleft(mat[r][c])
        ret = []
        for diag in ans:
            ret.extend(list(diag))
        return ret


# O(N) / O(1) excluding memory of what is returned; optimized with more complexity
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         if not mat or not mat[0]:
#             return []
#
#         n, m = len(mat), len(mat[0])
#         ret = []
#         for layer in range(n + m - 1):
#             # Determine the starting point and direction of the diagonal
#             if layer % 2 == 0:
#                 # Start from top to bottom on this diagonal
#                 r = min(layer, n - 1)
#                 c = layer - r
#                 while r >= 0 and c < m:
#                     ret.append(mat[r][c])
#                     r -= 1
#                     c += 1
#             else:
#                 # Start from bottom to top on this diagonal
#                 c = min(layer, m - 1)
#                 r = layer - c
#                 while c >= 0 and r < n:
#                     ret.append(mat[r][c])
#                     r += 1
#                     c -= 1
#
#         return ret
