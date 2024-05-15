from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, rem = 0, -1, k
        ans = 0

        while right < len(nums) - 1:
            if rem >= 0:
                right += 1
                rem -= 1 if nums[right] == 0 else 0
            while rem < 0:
                rem += 1 if nums[left] == 0 else 0
                left += 1
            ans = max(ans, right - left + 1)
        return ans
