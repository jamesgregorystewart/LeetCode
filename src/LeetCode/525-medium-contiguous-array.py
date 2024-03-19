from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        count, length = 0, 0
        for i, num in enumerate(nums):
            count = count - 1 if num == 0 else count + 1
            if count not in map:
                map[count] = i
            else:
                length = max(length, i - map[count])
        return length
