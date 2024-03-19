from typing import List
from collections import Counter

"""
slide a window with backtracking until the counter is empty; if found add starting index to result

slide a window with two loops; outer while loop with dynamic starting position, and a second inner for loop
that slides forward whenever an initial word is found and it slides n steps each time (the size of the words)
"""


# O(s * (s//n))
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = Counter(words)
        n = len(words[0])
        idx = 0
        result = []
        while idx <= len(s) - (n * len(words)):
            if s[idx : n + idx] in counter:
                print(s[idx : n + idx])
                counter_copy = counter.copy()
                for i in range(idx, len(s), n):
                    if counter_copy and s[i : n + i] not in counter_copy:
                        # there are words left but next word not in words
                        break
                    counter_copy[s[i : n + i]] -= 1
                    if counter_copy[s[i : n + i]] == 0:
                        # remove the word when there are no more counts of it
                        del counter_copy[s[i : n + i]]
                    if not counter_copy:
                        # we found all the words so append index and break
                        result.append(idx)
                        break
            idx += 1
        return result


solution = Solution()
print(solution.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
print(
    solution.findSubstring(
        "wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]
    )
)
print(solution.findSubstring(s="barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
