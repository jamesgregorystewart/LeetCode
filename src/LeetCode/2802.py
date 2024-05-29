"""
4 7 
44 47 74 77
444 447 474 477 744 747 774 777
4444 4447 4474 4477 4744 4747 4774 4777

x + cur


2^1 2
2^2 4
2^3 8
2^4

1) find the number of bits to make up the value
2) compute the number by iterating over it from leftmost to right most and setting each to 7 from 4


k = 7

cur = 7
"""


class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        base = 0
        rem = k
        while rem > 2 ** (base + 1):
            base += 1
            rem -= 2**base

        ans = ["4"] * (base + 1)
        rem -= 1

        for i in range(base, -1, -1):
            if rem >= 2**i:
                rem -= 2**i
                ans[base - i] = "7"

        return "".join(ans)
