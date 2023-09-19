# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
#
#  
#
# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
#  
#
# Constraints:
#
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#  
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
Idea: Frequency map with sort of frequencies -- O(nlog(n)) / O(n)

'''
import heapq
from typing import Dict, List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums 

        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)

        

solution = Solution()
print(solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
print(solution.topKFrequent(nums = [1], k = 1))
print(solution.topKFrequent(nums = [1,2], k = 2))
