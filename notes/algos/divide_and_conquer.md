# Divide and Conquer

## Intuition
Works in Two Phases
1. Divide the problem into subproblems
2. Repeatedly solve each subprobllem independently and combine the result to solve the original problem.

In the context of [Longest Substring with at Least K Repeating Characters](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/) we would recursively apply this strategy by splitting the string into substrings and combine the result to find the longest substring that satisfies the given condition. The longest substring for a string starting at index `start` and ending at index `end` can be given by, 
    `longestSubstring(start, end) = max(longestSubstring(start, mid), longestSubstring(mid+1, end))`

The string would only be split when we find an invalid characcter. An invalid character is the one with a fequency of less than `k`. Since the invalid character cannot be part of the result, we split the string at the index where we cfind the invalid character, recusively check for each split, and combine the result.

Algorithm:
1. Build the CountMap
2. Find the position for mid index. Iterate over the string until the first invalid character in the string, this is the `mid`.
3. Split the string into 2 substrinngs at the `mid` index and recursively find the result.

Solution:
```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = Counter(s)
        for c, v in counts.items():
            if v < k:
                # if count of char is less than k, it is invalid for string, so divide
                return max(
                    [self.longestSubstring(sub, k) for sub in s.split(c)]
                    if len(s) >= k
                    else [0]
                )
        # return the length of string where there are no invalid characters
        return len(s)
```
