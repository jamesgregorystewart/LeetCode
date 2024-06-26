from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def update(bits, num, change) -> None:
            for i in range(32):
                if (num >> i) & 1:
                    bits[i] += change

        def bitsToInt(bits) -> int:
            cur = 0
            for i in range(32):
                if bits[i]:
                    cur += 2**i
            return cur

        start = 0
        n = len(nums)
        ans = n + 1
        bits = [0] * 32

        for end in range(n):
            update(bits, nums[end], 1)
            while start <= end and bitsToInt(bits) >= k:
                ans = min(ans, end - start + 1)
                update(bits, nums[start], -1)
                start += 1
        return ans if ans < n + 1 else -1
