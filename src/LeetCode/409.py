from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        sum_even = 0
        has_odd = False

        for count in counter.values():
            if count % 2 == 0:
                sum_even += count
            else:
                sum_even += count - 1
                has_odd = True

        # If there's any character with an odd count, we can place one in the middle
        return sum_even + 1 if has_odd else sum_even
