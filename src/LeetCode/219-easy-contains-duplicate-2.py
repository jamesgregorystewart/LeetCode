from typing import List, Dict
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = defaultdict(int)
        for i, num in enumerate(nums):
            if num in map:
                if i - map[num] <= k:
                    return True
            map[num] = i
        return False
