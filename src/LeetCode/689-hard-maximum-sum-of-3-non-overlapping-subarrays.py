import itertools


# Sourced Solution
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):

        sm1 = sm2 = sm3 = 0

        acc = list(itertools.accumulate(nums, initial=0))

        for i, (a0, a1, a2, a3) in enumerate(
            zip(acc, acc[k:], acc[2 * k :], acc[3 * k :])
        ):
            if a1 - a0 > sm1:
                sm1, idx1 = a1 - a0, i

            if a2 - a1 > sm2 - sm1:
                sm2, idx2 = sm1 + a2 - a1, (idx1, i + k)

            if a3 - a2 > sm3 - sm2:
                sm3, idx3 = sm2 + a3 - a2, (*idx2, i + 2 * k)

        return idx3


# Attempt DP approach as well


solution = Solution()
print(solution.maxSumOfThreeSubarrays(nums=[1, 2, 1, 2, 6, 7, 5, 1], k=2))
