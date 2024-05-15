from typing import List


class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        N, M = len(encoded1), len(encoded2)
        i1 = i2 = 0
        ans = []

        prev_prod, prev_freq = None, 0
        while i1 < N and i2 < M:
            (v1, f1), (v2, f2) = encoded1[i1], encoded2[i2]
            if not prev_prod or v1 * v2 == prev_prod:
                prev_freq += min(f1, f2)
            else:
                ans.append([prev_prod, prev_freq])
                prev_freq = min(f1, f2)
            prev_prod = v1 * v2

            if f1 == f2:
                i1, i2 = i1 + 1, i2 + 1
            elif f1 < f2:
                i1 += 1
                encoded2[i2][1] -= f1
            else:
                i2 += 1
                encoded1[i1][1] -= f2
        if not ans or ans[-1][0] != prev_prod:
            ans.append([prev_prod, prev_freq])
        return ans
