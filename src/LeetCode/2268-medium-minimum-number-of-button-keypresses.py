import collections


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        counts = collections.Counter(s)
        counts_sorted = sorted([(count, c) for c, count in counts.items()])

        ans = 0
        for key_presses in range(1, 4):
            for _ in range(1, 10):
                if not counts_sorted:
                    return ans
                count, _ = counts_sorted.pop()
                ans += count * key_presses
        return ans
