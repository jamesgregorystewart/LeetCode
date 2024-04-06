from collections import Counter
from typing import List


# O(N + Mlog(M)) where M is the number of distinct elements
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         counts = Counter(s)
#         sorted_frequencies = sorted([(v, k) for k, v in counts.items()], reverse=True)
#         return "".join([c * freq for freq, c in sorted_frequencies])


# O(N) bucket sort
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        buckets: List[List[str]] = [[] for _ in range(max_freq + 1)]
        for c, freq in counts.items():
            buckets[freq].append(c)

        result = []
        for freq, c_list in enumerate(buckets):
            for c in c_list:
                result.append(c * freq)
        return "".join(result[::-1])


solution = Solution()
print(solution.frequencySort("tree"))
