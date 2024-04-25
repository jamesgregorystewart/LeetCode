from typing import List


# O(nlogn) solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for i in range(len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
                continue
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans


solution = Solution()
print(solution.merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
print(solution.merge(intervals=[[1, 4], [4, 5]]))
print(solution.merge(intervals=[[1, 4], [0, 4]]))
