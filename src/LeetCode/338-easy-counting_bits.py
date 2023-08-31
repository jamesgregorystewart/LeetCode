# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
#
#  
#
# Example 1:
#
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:
#
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
#  
#
# Constraints:
#
# 0 <= n <= 105
#  
#
# Follow up:
#
# It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


"""
Idea: Use previously calculated values. Single pass solution.

Time: O(n)
Space: O(n)
"""

from typing import List
from math import floor, log

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        if n == 2:
            return [0, 1, 1]
        ans = [0, 1, 1]
        for i in range(3, n+1):
            max_power = floor(log(i, 2))
            ans.append(1) if i == 2**max_power else ans.append(ans[(i - 2**max_power)] + 1)

        return ans


solution = Solution()
print(solution.countBits(2))
print(solution.countBits(5))
print(solution.countBits(123))
print(solution.countBits(605)[605])
