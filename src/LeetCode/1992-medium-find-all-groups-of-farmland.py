from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        farms = []
        n, m = len(land), len(land[0])

        def map_farm(sr, sc):
            n, m = len(land), len(land[0])
            r, c = sr, sc
            er, ec = sr, sc
            while r < n and c < m and land[r][c] == 1:
                while r < n and c < m and land[r][c] == 1:
                    land[r][c] = 0
                    ec = max(ec, c)
                    c += 1
                er = max(er, r)
                r += 1
                c = sc
            return (sr, sc, er, ec)

        for r in range(n):
            for c in range(m):
                if land[r][c] == 1:
                    farms.append(map_farm(r, c))
        return farms
