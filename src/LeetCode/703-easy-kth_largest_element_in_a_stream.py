import heapq
from typing import List

"""
Tricks:
    - performing heap operations on a list means all added elements will be heap-sorted
        but not the elements initially comprising the list until it has been heapified
    - starting from an empty list, a heapify is not required
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        for num in nums:
            if len(self.min_heap) < self.k:
                heapq.heappush(self.min_heap, num)
            elif num > self.min_heap[0]:
                heapq.heappushpop(self.min_heap, num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
