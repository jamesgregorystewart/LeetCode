class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        for i, c in enumerate(s):
            if k == 0:
                break
            c_val = ord(c) - ord("a")
            for j in range(27):
                diff = min(abs(c_val - j), abs(c_val - (j + 26)))
                if diff <= k:
                    k -= diff
                    s = s[:i] + chr(j + ord("a")) + s[i + 1 :]
                    break
        return s


solution = Solution()
print(solution.getSmallestString(s="zbbz", k=3))
print(solution.getSmallestString(s="xaxcd", k=4))
print(solution.getSmallestString(s="lol", k=0))
print(solution.getSmallestString(s="lol", k=5))
