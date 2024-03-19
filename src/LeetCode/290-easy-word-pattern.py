from typing import Dict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word: Dict[str, str] = {}
        word_to_pattern: Dict[str, str] = {}
        words = s.split(" ")
        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in pattern_to_word and words[i] not in word_to_pattern:
                pattern_to_word[pattern[i]] = words[i]
                word_to_pattern[words[i]] = pattern[i]
            elif (
                pattern[i] not in pattern_to_word
                or words[i] not in word_to_pattern
                or pattern_to_word[pattern[i]] != words[i]
                or word_to_pattern[words[i]] != pattern[i]
            ):
                return False

        return True
