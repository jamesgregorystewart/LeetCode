from sortedcontainers import SortedDict
from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        map = SortedDict()
        ans = []
        for num, freq in zip(nums, freq):
            if num not in map:
                map[num] = freq
            else:
                map[num] += freq
            _, highest_freq = map.peekitem(index=-1)
            ans.append(highest_freq)

        return ans


solution = Solution()
print(solution.mostFrequentIDs(nums=[2, 3, 2, 1], freq=[3, 2, -3, 1]))
