from typing import List


class Solution:
    def __init__(self) -> None:
        self.winner = {3: "Bronze Medal", 2: "Silver Medal", 1: "Gold Medal"}

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        min_score = min(score)
        max_score = max(score)
        score_to_index = [-1] * (max_score - min_score + 1)

        for i, s in enumerate(score):
            score_to_index[s - min_score] = i

        place = len(score)
        ans = ["" for _ in range(len(score))]
        for i in score_to_index:
            if i == -1:
                continue
            if place <= 3:
                ans[i] = self.winner[place]
            else:
                ans[i] = str(place)
            place -= 1
        return ans
