"""

2736
7236

2939
9932

"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(d) for d in str(num)]
        max_i = len(nums) - 1
        left = right = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[max_i]:
                max_i = i
            if nums[i] < nums[max_i]:
                left = i
                right = max_i
        nums[left], nums[right] = nums[right], nums[left]
        return int("".join(str(s) for s in nums))
