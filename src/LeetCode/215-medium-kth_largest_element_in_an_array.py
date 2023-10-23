# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?
#
#  
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#  
#
# Constraints:
#
# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap: List[int] = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif min_heap and num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return heapq.heappop(min_heap)

solution = Solution()
print(solution.findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 4))
