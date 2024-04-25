import collections
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        max_heap = []
        for k, count in counts.items():
            heapq.heappush(max_heap, (-count, k))

        ans = []
        while max_heap:
            c1, v1 = heapq.heappop(max_heap)
            if not max_heap:
                if c1 < -1:
                    return ""
                else:
                    ans.append(v1)
                    break
            c2, v2 = heapq.heappop(max_heap)
            ans.extend([v1, v2])
            if c1 < -1:
                heapq.heappush(max_heap, (c1 + 1, v1))
            if c2 < -1:
                heapq.heappush(max_heap, (c2 + 1, v2))
        return "".join(ans)
