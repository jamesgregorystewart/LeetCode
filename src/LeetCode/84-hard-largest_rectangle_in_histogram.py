""" 84 HARD Largest Rectangle in Histogram """


# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
#
#  
#
# Example 1:
#
#
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:
#
#
# Input: heights = [2,4]
# Output: 4
#  
#
# Constraints:
#
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

from typing import List
from collections import namedtuple

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        Block = namedtuple("Block", ["position", "height", "width"])
        blocks, max_area = [], float("-inf")

        for rectangle_position, rectangle in enumerate(heights):
            cur_block = Block(rectangle_position, rectangle, 1)
            # while there are blocks and the previous block goes up to just before the curr rectangle
            if blocks and cur_block.position - (blocks[-1].position + blocks[-1].width) == 0:
                prev_block = blocks[-1]
                # if combining cur rectangle with previous block has more area, then do so
                combined_block = Block(prev_block.position, min(cur_block.height, prev_block.height), prev_block.width + 1)
                if combined_block.height * combined_block.width >= (prev_block.height * prev_block.width) and combined_block.height * combined_block.width > (cur_block.height * cur_block.width):
                    prev_block = blocks.pop()
                    cur_block = combined_block
            blocks.append(cur_block)
            max_area = max(max_area, (cur_block.height * cur_block.width))
            # print(blocks)

        # Final check is to go through the stack, and seeing if there is an underlying, low-height but wide max
        prev_block = blocks.pop()
        max_area_seen, min_height, running_length = prev_block.height * prev_block.width, prev_block.height, prev_block.width
        while blocks:
            cur_block = blocks.pop()
            min_height = min(min_height, cur_block.height) if cur_block.height > 0 else float("inf")
            running_length = running_length + cur_block.width if cur_block.height > 0 else 0
            max_area_seen = max(max_area_seen, min_height * running_length)

        return max(max_area, max_area_seen)

from itertools import chain

class BetterSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # list[(column, height)]
        
        for i, height in enumerate(chain([0], heights, [0])): # append zero heights at both ends
            while stack and stack[-1][1] > height:
                rect_right = i
                rect_height = stack.pop()[1]
                rect_left = stack[-1][0]
                area = (rect_right - rect_left - 1) * rect_height
                maxArea = max(area, maxArea)
            
            stack.append((i, height))
            
        return maxArea

# solution = Solution()
# print(solution.largestRectangleArea([2,1,5,6,2,3]))
# print(solution.largestRectangleArea([2,1,5,6,2,3,1,2,1,5,6,2,3]))
# print(solution.largestRectangleArea([1,2,3]))
# print(solution.largestRectangleArea([1,2,3,4,5]))

solution = BetterSolution()
print(solution.largestRectangleArea([1,2,3,4,5]))
print(solution.largestRectangleArea([2,1,5,6,2,3]))
print(solution.largestRectangleArea([2,1,5,6,2,3,1,2,1,5,6,2,3]))

