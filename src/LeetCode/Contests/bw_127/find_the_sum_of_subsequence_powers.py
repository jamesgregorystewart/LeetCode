import functools
from typing import List


# O(N(choose K) * dGKlog(K) + N(choose K) * k + N(choose K)); TLE
# class Solution:
#     def sumOfPowers(self, nums: List[int], k: int) -> int:
#         def backtrack(start, subsequence):
#             if len(subsequence) == k:
#                 subsequences.append(sorted(subsequence[:]))
#                 return
#
#             for i in range(start, len(nums)):
#                 subsequence.append(nums[i])
#                 backtrack(i + 1, subsequence)
#                 subsequence.pop()
#
#         subsequences = []
#         backtrack(0, [])
#
#         # step 2 calculate sumOfPowers
#         powers = []
#         for subsequence in subsequences:
#             min_abs_val = float("inf")
#             for i in range(len(subsequence) - 1):
#                 min_abs_val = min(min_abs_val, abs(subsequence[i] - subsequence[i + 1]))
#             powers.append(min_abs_val)
#
#         # step 3 return sum
#         return sum(powers) % (10**9 + 7)

from functools import lru_cache


# DP solution
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0

        @lru_cache(None)
        def dp(idx, min_diff, last_choose, left_k):
            if left_k == 0:
                if min_diff != float("inf"):
                    return min_diff
                else:
                    return 0
            if idx == len(nums):
                return 0
            choose = dp(
                idx + 1,
                min(min_diff, abs(last_choose - nums[idx])),
                nums[idx],
                left_k - 1,
            )
            not_choose = dp(idx + 1, min_diff, last_choose, left_k)
            return (choose + not_choose) % MOD

        return dp(0, float("inf"), float("inf"), k)
