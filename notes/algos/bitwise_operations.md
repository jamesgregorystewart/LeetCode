# Bitwise Operations

Practical Applications:
- Setting a bit `num |= (1 << i)`
- Clearing a bit `num &= ~(1 << i)`
- Toggling a bit `num ^= (1 << i)`
- Checking a bit `(num & (1 << i)) != 0`

[Shortest Subarry with OR at Least K II](https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii)

```python
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
```
