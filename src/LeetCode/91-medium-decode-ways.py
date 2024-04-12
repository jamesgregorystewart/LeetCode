"""

11106

"""


# O(N)  O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        prev1, prev2 = 1, 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                prev1, prev2 = 0, prev1
                continue
            if int(s[i]) >= 3:
                prev2 = prev1
            if 10 <= int(s[i : i + 2]) <= 26:
                prev1, prev2 = prev1 + prev2, prev1

        return prev1


# O(2^N)
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         def dfs(i) -> None:
#             if i == len(s):
#                 self.ans += 1
#                 return
#
#             if s[i] == "0":
#                 return
#             dfs(i + 1)
#             if i < len(s) - 1 and 0 < int(s[i : i + 2]) < 27:
#                 dfs(i + 2)
#
#         self.ans = 0
#         dfs(0)
#         return self.ans


solution = Solution()
print(solution.numDecodings(s="12"))
print(solution.numDecodings(s="11106"))
print(solution.numDecodings(s="226"))
print(solution.numDecodings(s="06"))
print(solution.numDecodings(s="1123"))
print(solution.numDecodings(s="123123"))
