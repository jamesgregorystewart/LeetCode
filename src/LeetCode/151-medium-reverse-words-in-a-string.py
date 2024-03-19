class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip(" ")
        parts = s.split(" ")
        parts = [s for s in parts if s != ""]
        parts = parts[::-1]
        return " ".join(parts)


solution = Solution()
print(solution.reverseWords("a good   example"))
