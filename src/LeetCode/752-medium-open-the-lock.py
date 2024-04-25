import collections
from collections.abc import Collection
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        if "0000" in deadends_set:
            return -1
        visited = set()
        visited.add("0000")
        q = collections.deque(["0000"])
        turns = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return turns
                for digit in range(4):
                    for op in [-1, 1]:
                        next_combo = (
                            cur[:digit]
                            + str((int(cur[digit]) + op) % 10)
                            + cur[digit + 1 :]
                        )
                        if next_combo not in visited and next_combo not in deadends_set:
                            visited.add(next_combo)
                            q.append(next_combo)
            turns += 1
        return -1
