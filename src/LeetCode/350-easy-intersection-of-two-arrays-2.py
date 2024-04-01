from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        return [
            key
            for key, value in counter1.items()
            if key in counter2
            for _ in range(min(value, counter2[key]))
        ]
