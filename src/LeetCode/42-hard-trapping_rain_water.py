""" HARD - Trapping Rain Water """

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9

"""
Idea:
    - l and r pointers go from left to right; track max volume between both
    - when r is equal to or greater than l, set l = r; r = r+1
    - loop while r less than len(height)
    - identify global maximum, if there are 2, choose right

Time: O(n)
Space: O(1)
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_vol = 0

        # Left to Right
        l, r = 0, 1
        global_max = 0
        container_vol = 0
        while r < len(height):
            global_max = r if height[r] >= height[global_max] else global_max
            if height[r] >= height[l]:
                container_vol = min(height[l], height[r]) * (r-l-1)
                for i in range(l+1, r):
                    container_vol -= height[i]
                max_vol += container_vol
                print("Trapped %s rain water in segment" % str(container_vol))
                l, r = r, r + 1
            else:
                r += 1
        
        # Right to Left
        l, r = len(height)-2, len(height)-1
        while l >= global_max:
            if height[l] >= height[r]:
                container_vol = min(height[l], height[r]) * (r-l-1)
                for i in range(r-1, l, -1):
                    container_vol -= height[i]
                max_vol += container_vol
                print("Trapped %s rain water in segment" % str(container_vol))
                l, r = l - 1, l
            else:
                l -= 1

        return max_vol

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap([4,2,0,3,2,5]))
print(solution.trap([]))
print(solution.trap([1,1]))
print(solution.trap([1]))
print(solution.trap([2,0,2]))
