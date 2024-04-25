from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        max_left, max_right = 0, 0

        while left < right:
            if height[left] < height[right]:
                ans += max_left - height[left] if max_left > height[left] else 0
                max_left = max(max_left, height[left])
                left += 1
            else:
                ans += max_right - height[right] if max_right > height[right] else 0
                max_right = max(max_right, height[right])
                right -= 1

        return ans
