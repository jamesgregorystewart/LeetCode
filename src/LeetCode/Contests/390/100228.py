class Solution:
    def minOperations(self, k: int) -> int:
        if k <= 1:
            return 0
        num = 2
        operations = 1
        while num < k:
            operations += 1
            num *= num
        return operations


solution = Solution()
print(solution.minOperations(11))
