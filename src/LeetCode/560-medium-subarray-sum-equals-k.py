from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = right = 0
        ans = 0
        sum = 0
        while left <= right and right < len(nums):
            sum += nums[right]
            if sum < k:
                right += 1
            elif sum == k:
                ans += 1
                sum -= nums[left]
                left += 1
            if sum > k:
                if sum - nums[right] < k:
                    sum -= nums[left]
                    left += 1
                else:
                    sum -= nums[right]
                    right -= 1
        return ans
