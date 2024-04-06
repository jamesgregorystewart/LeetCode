from typing import List


# O(N) bucket sort solution
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_val, min_val = max(nums), min(nums)
        buckets_size = abs(max_val - min_val)
        offset = min_val
        buckets = [0] * (buckets_size + 1)
        for num in nums:
            buckets[num - offset] += 1

        result = []
        for num, freq in enumerate(buckets):
            if freq:
                result.extend([num + offset] * freq)
        return result
