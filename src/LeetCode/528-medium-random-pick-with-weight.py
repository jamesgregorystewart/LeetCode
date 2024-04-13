from typing import List
import bisect
import random


# O(N + Plog(N))
class Solution:

    def __init__(self, w: List[int]) -> None:
        self.w = w
        self.probabilities = []
        total_weight = 0
        for weight in w:
            total_weight += weight
            self.probabilities.append(total_weight)

    def pickIndex(self) -> int:
        target = random.randint(1, self.probabilities[-1])
        target_index = bisect.bisect_left(self.probabilities, target)
        return target_index
