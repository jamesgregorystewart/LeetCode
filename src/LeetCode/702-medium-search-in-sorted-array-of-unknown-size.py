# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class Solution:
    def search(self, reader: "ArrayReader", target: int) -> int:
        left, right = 0, 10**4
        while left <= right:
            mid = (left + right) // 2
            mid_val = reader.get(mid)
            if mid_val == target:
                return mid
            if target < mid_val:
                right = mid - 1
            else:
                left = mid + 1
        return -1
