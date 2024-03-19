from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_sequence = 0
        for num in nums:
            sequence = 1
            if num + 1 in nums_set:
                continue
            cur = num
            while cur - 1 in nums_set:
                cur = cur - 1
                sequence += 1
            longest_sequence = max(longest_sequence, sequence)
        return longest_sequence


solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
print(solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
