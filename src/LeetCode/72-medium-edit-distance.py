class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dp(word: str) -> int:
            if word == word2:
                return 0

            for i in range(len(word1)):
                if i >= len(word2):
                    return dp(word[:i] + word[i + 1 :]) + 1
                if 
