# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
#
#
#
# Example 1:
#
# Input: num = 3
# Output: "III"
# Explanation: 3 is represented as 3 ones.
# Example 2:
#
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 3:
#
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#
#
# Constraints:
#
# 1 <= num <= 3999


from re import S


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        iteration = 1
        while num:
            digit = num % 10
            num //= 10
            if iteration == 1:
                if digit == 4:
                    roman += "VI"
                elif digit == 9:
                    roman += "XI"
                elif digit != 4 and digit != 9:
                    roman += "I" * (digit % 5)
                    if digit >= 5:
                        roman += "V"
            elif iteration == 2:
                if digit == 4:
                    roman += "LX"
                elif digit == 9:
                    roman += "CX"
                elif digit != 4 and digit != 9:
                    roman += "X" * (digit % 5)
                    if digit >= 5:
                        roman += "L"
            elif iteration == 3:
                if digit == 4:
                    roman += "DC"
                elif digit == 9:
                    roman += "MC"
                elif digit != 4 and digit != 9:
                    roman += "C" * (digit % 5)
                    if digit >= 5:
                        roman += "D"
            elif iteration == 4:
                roman += "M" * digit

            iteration += 1

        return roman[::-1]


solution = Solution()
print(solution.intToRoman(num=3))
print(solution.intToRoman(num=9))
print(solution.intToRoman(num=5))
print(solution.intToRoman(num=58))
print(solution.intToRoman(num=94))
print(solution.intToRoman(num=194))
print(solution.intToRoman(num=494))
print(solution.intToRoman(num=994))
print(solution.intToRoman(num=1994))
print(solution.intToRoman(num=3994))
