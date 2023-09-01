# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#  
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
#  
#
# Constraints:
#
# -231 <= x <= 231 - 1

"""
Idea:
    access last digit with x % 10; remove last digit with x //= 10

Time: O(n) where n is bits in x; technically O(1) since 32 bit maximum
Space: O(1) 
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        res = 0
        x = abs(x)
        while x:
            res = (res * 10) + (x % 10)
            x //= 10

        return 0 if abs(res) > 2**31 else res * sign
       

solution = Solution()
print(solution.reverse(123))
print(solution.reverse(-123))
print(solution.reverse(2147483638))
print(solution.reverse(-2147483638))
