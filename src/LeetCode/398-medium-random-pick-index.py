from collections import defaultdict
from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.map = defaultdict(list)

        for i, num in enumerate(nums):
            self.map[num].append(i)

    def pick(self, target: int) -> int:
        target_index = random.randint(0, len(self.map[target]) - 1)
        return self.map[target][target_index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
