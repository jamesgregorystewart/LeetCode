""" 239 HARD Sliding Window Maximum """

# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
#
# Return the max sliding window.
#
#  
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
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
# 1 <= k <= nums.length

"""
Idea:
    - Monotonic deque to store window values
    - Add indices to deque in monotonic order
    - Remove leftmost value if it falls out of the window during iteration

Time: O(n) because each element can only be added to the deque once, which means the deque is llimited to n pushes.
Space: O(k)
"""

from typing import List
from collections import deque
import functools

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def addToDeque(dq: deque[int], i: int) -> None:
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)

        dq = deque()
        res = []
        # initialize first k values
        for i in range(k):
            addToDeque(dq, i)
        res.append(nums[dq[0]])

        for i in range(k, len(nums)):
            addToDeque(dq, i)
            # Remove the leftmost elements which are out of the window range
            while dq[0] < i - k + 1:
                dq.popleft()
            res.append(nums[dq[0]])

        return res


solution = Solution()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(solution.maxSlidingWindow([1,2,3,4,5,6,7,8], 2))
