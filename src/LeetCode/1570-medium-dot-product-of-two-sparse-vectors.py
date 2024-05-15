from typing import List
import functools


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, v in enumerate(nums):
            self.vector[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        for k, v in vec.vector.items():
            if k in self.vector:
                self.vector[k] *= v
        return sum(self.vector.values())


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
