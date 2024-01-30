# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
#
# Input: n = 1
# Output: [["Q"]]
#
#
# Constraints:
#
# 1 <= n <= 9

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(x, queens, config):
            if len(config) == n:
                ans.append(config)
                return
            for i in range(n):
                if safe((x, i), queens):
                    row = "." * n
                    row = row[:i] + "Q" + row[i + 1 :]
                    backtrack(x + 1, queens + [(x, i)], config + [row])

        def safe(position, queens) -> bool:
            for queen in queens:
                """
                Two points are diagonal to each other if the abs diff of in the x-coords
                and y-coords are equivalent. This is because in a plane, a diagonal
                in a square or a rectangle has equal horizontal and vertical distances
                """
                if position[1] == queen[1] or abs(position[0] - queen[0]) == abs(
                    position[1] - queen[1]
                ):
                    return False
            return True

        ans: List[List[str]] = []
        backtrack(0, [], [])
        return ans


solution = Solution()
print(solution.solveNQueens(n=4))
