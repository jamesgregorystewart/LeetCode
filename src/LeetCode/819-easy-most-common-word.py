from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)

        # convert to lower case and split string into words by spaces and punctuation
        a = re.split(r"\W+", paragraph.lower())

        # make new list consisitng of words not in banned list (remove banned words)
        b = [w for w in a if w not in banned_set and len(w) > 0]

        # return value that counted max times in the new list
        return max(b, key=b.count)
