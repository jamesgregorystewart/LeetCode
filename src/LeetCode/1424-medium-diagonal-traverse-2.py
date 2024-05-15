import collections
from typing import List


# O(N * M) where M is max column
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        R, C = len(nums), max(len(row) for row in nums)

        ans = []
        for i in range(R):
            r, c = i, 0
            while r >= 0 and c < C:
                if c < len(nums[r]):
                    ans.append(nums[r][c])
                r, c = r - 1, c + 1

        for i in range(1, C):
            r, c = R - 1, i
            while r >= 0 and c < C:
                if c < len(nums[r]):
                    ans.append(nums[r][c])
                r, c = r - 1, c + 1
        return ans


# O(N) solution BFS
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = collections.deque([(0, 0)])
        seen = set([(0, 0)])
        ans = []

        while q:
            r, c = q.popleft()
            ans.append(nums[r][c])

            if r < len(nums) - 1 and c < len(nums[r + 1]) and (r + 1, c) not in seen:
                seen.add((r + 1, c))
                q.append((r + 1, c))

            if c + 1 < len(nums[r]) and (r, c + 1) not in seen:
                seen.add((r, c + 1))
                q.append((r, c + 1))
        return ans
