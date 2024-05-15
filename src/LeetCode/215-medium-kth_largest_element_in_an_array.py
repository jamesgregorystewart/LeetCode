from typing import List
import heapq


# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         min_heap: List[int] = []
#         for num in nums:
#             if len(min_heap) < k:
#                 heapq.heappush(min_heap, num)
#             elif min_heap and num > min_heap[0]:
#                 heapq.heappushpop(min_heap, num)
#
#         return heapq.heappop(min_heap)


# Counting Sort O(N + M) where M is max_v - min_v
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_v, min_v = max(nums), min(nums)
        counts = [0] * (max_v - min_v + 1)

        for num in nums:
            counts[num - min_v] += 1

        jth = 0
        for i in range(len(counts) - 1, -1, -1):
            jth += counts[i]
            if jth >= k:
                print(i)
                return i + min_v
        return counts[min_v]


solution = Solution()
print(solution.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
