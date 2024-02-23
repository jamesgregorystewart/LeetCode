# Palindromes

## Approaches
Approaches to consider when solving a Palindrome problem:

1. Brute Force: O(N^3) / O(1)
2. Dynamic Programming: O(N^2) / O(N^2)
3. Expand around Center: O(N^2) / O(1)

There are other more complex, sub-quadratic solutions which would be difficult to implment in an interview.

## Example Problems

[Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/)

# Dynamic Programming Solution
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = n
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        # 2-length
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                ans += 1

        # 3+ length
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    ans += 1

        return ans
```

# Expand Around Center
``` python
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        self.n = len(s)
        for i in range(self.n - 1):
            ans += self.expand(s, i, i)
            ans += self.expand(s, i, i + 1)
        ans += self.expand(s, self.n - 1, self.n - 1)

        return ans

    def expand(self, ss: str, lo: int, hi: int) -> int:
        res = 0
        while lo >= 0 and hi < self.n:
            if ss[lo] != ss[hi]:
                break
            lo -= 1
            hi += 1
            res += 1
        return res
```
