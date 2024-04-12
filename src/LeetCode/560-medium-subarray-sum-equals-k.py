from typing import List

"""

1 2 3 

3 2 1

-1 0 1 1 1  k = 2

-1: 2
0: 1
1: 1
2: 1



current_sum = -1
ans = 3

"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_sums = {0: 1}
        currentSum = 0
        ans = 0
        for num in nums:
            currentSum += num
            if currentSum - k in subarray_sums:
                ans += subarray_sums[currentSum - k]
            subarray_sums[currentSum] = subarray_sums.get(currentSum, 0) + 1
        return ans
