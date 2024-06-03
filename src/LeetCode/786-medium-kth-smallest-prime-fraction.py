from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = []
        N = len(arr)
        ans.append(arr[N % k])
