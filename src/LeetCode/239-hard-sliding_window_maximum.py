from typing import List
from collections import deque


# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         def addToDeque(dq: deque[int], i: int) -> None:
#             while dq and nums[i] > nums[dq[-1]]:
#                 dq.pop()
#             dq.append(i)
#
#         dq = deque()
#         res = []
#         # initialize first k values
#         for i in range(k):
#             addToDeque(dq, i)
#         res.append(nums[dq[0]])
#
#         for i in range(k, len(nums)):
#             addToDeque(dq, i)
#             # Remove the leftmost elements which are out of the window range
#             while dq[0] < i - k + 1:
#                 dq.popleft()
#             res.append(nums[dq[0]])
#
#         return res

import heapq
from collections import defaultdict


# O(N * log(K)) solution ~ O(N * log(N))
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if k == 1:
#             return nums
#         max_heap = [num * -1 for num in nums[:k]]
#         heapq.heapify(max_heap)
#         removed = defaultdict(int)
#
#         n = len(nums)
#         result = []
#         for i in range(k, n + 1):
#             while (max_val := -max_heap[0]) in removed and removed[max_val]:
#                 removed[max_val] -= 1
#                 heapq.heappop(max_heap)
#                 continue
#             result.append(max_val)
#
#             if i == n:
#                 break
#
#             removed[nums[i - k]] += 1
#             heapq.heappush(max_heap, nums[i] * -1)
#         return result

from collections import deque


# O(N) / O(K); Monotonic Stack
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if q and q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                result.append(nums[q[0]])

        return result


solution = Solution()
print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(solution.maxSlidingWindow([1, 2, 3, 4, 5, 6, 7, 8], 2))
