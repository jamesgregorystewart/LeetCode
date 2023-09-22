""" Container With Most Water """

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1
#  
#
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

"""
Idea:
    - Two pointers, move the pointer on the element with least height inward
    - Maintain max area (the min height of the two pointers * their distance from each other)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l, r = 0, len(height)-1
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r-l))
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
print(solution.maxArea([1,1]))
print(solution.maxArea([]))
