from typing import List


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        def isprime(num) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 1
            return True

        while left < right:
            left_prime = isprime(nums[left])
            right_prime = isprime(nums[right])
            if left_prime and right_prime:
                break
            if not left_prime:
                left += 1
            if not right_prime:
                right -= 1

        return right - left
