# Given two integers a and b, return the sum of the two integers without using the operators + and -.
#
#  
#
# Example 1:
#
# Input: a = 1, b = 2
# Output: 3
# Example 2:
#
# Input: a = 2, b = 3
# Output: 5
#  
#
# Constraints:
#
# -1000 <= a, b <= 1000

"""
Idea:

"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)

        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # Sum two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1
        else:
            # Subtract two positive integers 
            while y:
                x, y = x ^ y, ((~x) & y) << 1
        return x * sign

solution = Solution()
print(solution.getSum(1, 2))
print(solution.getSum(2, 1))
print(solution.getSum(14, -16))
print(solution.getSum(14, -16))
print(solution.getSum(-1, 0))
print(solution.getSum(0, -1))

