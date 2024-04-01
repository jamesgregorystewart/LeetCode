from typing import List


# O (n) / O(n)
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        if len(possible) == 2 and (possible[0] == 0 or possible[0] == possible[1] == 1):
            return -1
        bob_points = [0]
        reverse_possible = list(reversed(possible))
        cur = 0
        for i in range(1, len(reverse_possible)):
            cur = cur + 1 if reverse_possible[i - 1] == 1 else cur - 1
            bob_points.append(cur)

        daniel_cur = 0
        for i, level in enumerate(possible[: len(possible) - 1]):
            daniel_cur = daniel_cur + 1 if level == 1 else daniel_cur - 1
            if daniel_cur > bob_points[len(possible) - 1 - i]:
                return i + 1
        return -1
