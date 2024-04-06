from typing import List


# O(N) / O(M) where M is the range max-min; Memory overflow
# class Solution:
#     def maximumGap(self, nums: List[int]) -> int:
#         max_val, min_val = max(nums), min(nums)
#         buckets = [False] * (max_val - min_val + 1)
#
#         for num in nums:
#             buckets[num - min_val] = True
#
#         prev = max_val - min_val
#         max_gap = 0
#         for i in range(len(buckets) - 1, -1, -1):
#             if buckets[i]:
#                 max_gap = max(max_gap, prev - i)
#                 prev = i
#         return max_gap


# O(N + b) ~ O(b) / O(b)
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_val, min_val = max(nums), min(nums)
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        num_of_buckets = (max_val - min_val) // bucket_size + 1
        bucket_min = [float("inf")] * num_of_buckets
        bucket_max = [float("-inf")] * num_of_buckets

        for num in nums:
            bucket_idx = (num - min_val) // bucket_size
            bucket_min[bucket_idx] = min(bucket_min[bucket_idx], num)
            bucket_max[bucket_idx] = max(bucket_max[bucket_idx], num)

        prev_bucket_max = min_val
        max_gap = 0
        for i in range(num_of_buckets):
            if bucket_min[i] == float("inf") and bucket_max[i] == float("-inf"):
                continue

            max_gap = max(max_gap, bucket_min[i] - prev_bucket_max)
            prev_bucket_max = bucket_max[i]

        return max_gap
