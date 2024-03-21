import heapq
from typing import List

"""
Tricks:
    - performing heap operations on a list means all added elements will be heap-sorted
        but not the elements initially comprising the list until it has been heapified
    - starting from an empty list, a heapify is not required
"""
# Heap Solution O(Nlog(N) + Mlog(k)) where N is len of nums and M is the number of calls to add()
# class KthLargest:
#
#     def __init__(self, k: int, nums: List[int]):
#         self.min_heap = []
#         self.k = k
#         for num in nums:
#             if len(self.min_heap) < self.k:
#                 heapq.heappush(self.min_heap, num)
#             elif num > self.min_heap[0]:
#                 heapq.heappushpop(self.min_heap, num)
#
#     def add(self, val: int) -> int:   
#         if len(self.min_heap) < self.k:
#             heapq.heappush(self.min_heap, val)
#         elif val > self.min_heap[0]:
#             heapq.heappushpop(self.min_heap, val)
#         return self.min_heap[0]
class TreeNode:
    def __init__(self, val, left = None, right = None, smaller = 0, greater = 0) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.smaller = smaller
        self.greater = greater


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.root = TreeNode(nums[0]) if nums else None
        

    def add(self, val: int) -> int:


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
