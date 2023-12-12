from typing import List


def max_wine_profit(wines: List[int]) -> int:
    dp: List[List[int]] = [[0] * (len(wines)+1) for _ in range(len(wines)+1)]
    for l in range(len(wines)-1, -1, -1):
        for r in range(l, len(wines)):
            y = r + 1 - l
            dp[l][r] = max(
                dp[l+1][r] + (wines[l]*y),
                dp[l][r-1] + (wines[r]*y)
            )
    return dp[0][len(wines)-1]


print(max_wine_profit(wines=[2, 4, 6, 2, 5]))
