from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        bucket = {}
        diff = valueDiff + 1
        mini = min(nums)  # to normalize values

        def getKey(num: int) -> int:
            return (num - mini) // diff

        for i, num in enumerate(nums):
            key = getKey(num)
            if key in bucket:
                return True
            if key - 1 in bucket and abs(num - bucket[key - 1]) < diff:
                return True
            if key + 1 in bucket and abs(num - bucket[key + 1]) < diff:
                return True
            if i >= indexDiff:
                del bucket[getKey(nums[i - indexDiff])]
            bucket[key] = num
        return False
