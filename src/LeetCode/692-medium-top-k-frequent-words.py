from typing import List
from collections import Counter

"""
i: 2
love: 2
leetcode: 1
coding: 1

max = 2; min = 1
[_,_]
"""


# O(N + N + Klog(M))
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        buckets: List[List[str]] = [[] for _ in range(max(counts.values()) + 1)]

        for word, count in counts.items():
            buckets[count].append(word)

        result: List[str] = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                buckets[i].sort()
                result.extend(buckets[i][: k - len(result)])
            if len(result) >= k:
                break
        return result[:k]
