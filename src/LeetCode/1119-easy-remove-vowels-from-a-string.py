class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = set("aeiou")
        return "".join([c for c in s if c not in vowels])
