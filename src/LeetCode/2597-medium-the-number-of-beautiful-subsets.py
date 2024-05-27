import collections
from typing import List


"""

[2,4,6]


"""


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()

        def helper(i, seen):
            if seen:
                self.ans += 1

            for j in range(i, len(nums)):
                num = nums[j]
                if num - k not in seen:
                    seen[num] += 1
                    helper(j + 1, seen)
                    seen[num] -= 1
                    if seen[num] == 0:
                        del seen[num]

        self.ans = 0
        seen = collections.defaultdict(int)
        helper(0, seen)
        return self.ans
