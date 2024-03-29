# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
#
# Constraints:
#
# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105


from typing import List
import bisect


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        insert_index = bisect.bisect_left(intervals, newInterval)
        intervals.insert(insert_index, newInterval)
        ans: List[int] = []

        for i in range(len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

        return ans


# class Solution:
#     def insert(
#         self, intervals: List[List[int]], newInterval: List[int]
#     ) -> List[List[int]]:
#         ans = []
#         insert_interval = newInterval
#         inserted = False
#         for interval in intervals:
#             if (newInterval[1] >= interval[0] and newInterval[1] <= interval[1]) or (
#                 newInterval[0] >= interval[0]
#                 and newInterval[0] <= interval[1]
#                 or (newInterval[0] <= interval[0] and newInterval[1] >= interval[1])
#             ):
#                 # there is overlap
#                 insert_interval = [
#                     min(interval[0], insert_interval[0]),
#                     max(interval[1], insert_interval[1]),
#                 ]
#                 inserted = True
#             else:
#                 if inserted:
#                     ans.append(insert_interval)
#                 ans.append(interval)
#         if not inserted:
#             if not intervals or intervals[0][0] > newInterval[1]:
#                 return [newInterval] + intervals
#             else:
#                 return intervals + [newInterval]
#         return ans


solution = Solution()
print(solution.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(
    solution.insert(
        intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]
    )
)
