# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
#
# Input: digits = ""
# Output: []
# Example 3:
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
# Constraints:
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

"""
1) create mapping of num to letters
2) start with empty string in list
3) for each digit in the number:
    for 
        copy = ans.copy()
        ext = [combo + []]
"""

from typing import List


# Iterative solution
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         digit_map = {
#             "2": ["a", "b", "c"],
#             "3": ["d", "e", "f"],
#             "4": ["g", "h", "i"],
#             "5": ["j", "k", "l"],
#             "6": ["m", "n", "o"],
#             "7": ["p", "q", "r", "s"],
#             "8": ["t", "u", "v"],
#             "9": ["w", "x", "y", "z"],
#         }
#         build: List[str] = [""]
#         for digit in digits:
#             copy = build.copy()
#             for letter in digit_map[digit]:
#                 ext = [e + letter for e in copy]
#                 build.extend(ext)
#         return [e for e in build if len(e) == len(digits)]


# Backtracking Solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtracking(index, path):
            if len(path) == len(digits):
                combinations.append(path)
                return
            for letter in digit_map[digits[index]]:
                backtracking(index + 1, path + letter)

        combinations: List[str] = []
        backtracking(0, "")
        return combinations


solution = Solution()
print(solution.letterCombinations(digits="23"))
