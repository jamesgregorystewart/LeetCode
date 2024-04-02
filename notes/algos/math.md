# Tips and Tricks for problems with Math


[Problem](https://leetcode.com/problems/count-alternating-subarrays)
```python
class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:

        def addCount(left, right) -> None:
            length = right - left + 1
            self.ans += length * (length - 1) // 2

        prev = -1
        left = 0
        self.ans = 0
        for right in range(len(nums)):
            if nums[right] == prev:
                addCount(left, right)
                left = right
            else:
                prev = nums[right]

        addCount(left, len(nums))
        return self.ans
```

Instead of summing all values from 1:(right-left + 1) we can use the formula N * (N+1) // 2 to find the sum of all the natural numbers from 1:N (inclusive)

[Minimize Manhattan Distances](https://leetcode.com/problems/minimize-manhattan-distances)

Didn't solve this hard one, but it's interesting.
