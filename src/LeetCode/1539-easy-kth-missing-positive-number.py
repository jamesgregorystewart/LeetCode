from typing import List


# class Solution:
#     def findKthPositive(self, arr: List[int], k: int) -> int:
#         i = 0
#         rem = k
#         for num in arr:
#             if num > i + 1:
#                 if num - i + 1 > rem:
#                     return i + rem
#                 rem -= num - i - 1
#
#             i = num
#         return i + rem


# O(log(N))
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if arr and arr[0] > k:
            return k
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] - (mid + 1) >= k:
                right = mid - 1
            else:
                left = mid
        if arr[right] - (right + 1) < k:
            return arr[right] + (k - (arr[right] - (right + 1)))
        return arr[left] + (k - (arr[left] - (left + 1)))
