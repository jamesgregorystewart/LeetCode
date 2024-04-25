import collections
from typing import List


class Solution:
    def mostVisitedPattern(
        self, username: List[str], timestamp: List[int], website: List[str]
    ) -> List[str]:
        user_activity = collections.defaultdict(list)
        for user, ts, site in zip(username, timestamp, website):
            user_activity[user].append((ts, site))

        counts = collections.defaultdict(int)
        user_tupes = set()
        max_tupe = 0
        for user, activity in user_activity.items():
            if len(activity) < 3:
                continue
            activity.sort()
            for i in range(len(activity) - 2):
                for j in range(i + 1, len(activity) - 1):
                    for k in range(j + 1, len(activity)):
                        tupe = (activity[i][1], activity[j][1], activity[k][1])
                        user_tupes.add(tupe)
            for tupe in user_tupes:
                counts[tupe] += 1
                max_tupe = max(max_tupe, counts[tupe])
            user_tupes.clear()
        return min([tupe for tupe, count in counts.items() if count == max_tupe])
