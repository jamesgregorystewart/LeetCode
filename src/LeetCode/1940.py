from typing import List
import heapq


# class Solution:
#     def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
#         pointers = [0] * len(arrays)
#         min_heap = []
#         min_v, max_v = float('inf'), float('-inf')
#         for i in range(len(pointers)):
#             min_v = min(min_v, arrays[i][0])
#             max_v = max(max_v, arrays[i][0])
#             heapq.heappush(min_heap, arrays[i][pointers[i]])
#
#         ans = []
#         offset = 0
#         while True:
#             if min_v == max_v:
#                 ans.append(min_v)
#                 offset +=1
#             else:


class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        candidates = set(arrays[0])
        res = set(arrays[0])
        for arr in arrays[1:]:
            for e in arr:
                if e in candidates and not in res:
                    candidates.remove(e)
