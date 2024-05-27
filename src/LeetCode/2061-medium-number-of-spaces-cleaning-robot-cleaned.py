from typing import List

"""
1) simulate robot moves
2) save vectors as tuples in set; return ans when conflict
"""


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        vectors = {(0, 0)}  # direction, row | col
        ans = 1
        cur = (0, 0)
        room[0][0] = -1
        R, C = len(room), len(room[0])

        while True:
            print(cur, d, ans)
            r, c = cur[0] + directions[d][0], cur[1] + directions[d][1]
            if 0 <= r < R and 0 <= c < C and room[r][c] != 1:
                cur = (r, c)
                if room[cur[0]][cur[1]] == 0:
                    ans += 1
                room[cur[0]][cur[1]] = -1
            else:
                d = (d + 1) % 4
                if (d in [0, 2] and (d, cur[0]) in vectors) or (
                    d in [1, 3] and (d, cur[1]) in vectors
                ):
                    return ans
                vectors.add((d, cur[0] if d in [0, 2] else cur[1]))
