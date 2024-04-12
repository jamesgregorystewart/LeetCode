from collections import deque

"""
1234567

1

One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven

"""


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        lower = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        suffixes = {1: "Thousand", 2: "Million", 3: "Billion"}

        def parse(section, suffix_index) -> None:
            lower_i = section % 100
            if section and suffix_index:
                self.ans.appendleft(suffixes[suffix_index])
            if lower_i <= 19 and lower_i > 0:
                self.ans.appendleft(lower[lower_i])
            elif lower_i > 19:
                ones = lower_i % 10
                tens_index = lower_i // 10
                if ones:
                    self.ans.appendleft(lower[ones])
                self.ans.appendleft(tens[tens_index])
            upper = section // 100
            if upper > 0:
                self.ans.appendleft("Hundred")
                self.ans.appendleft(lower[upper])

        self.ans = deque()
        suffix_index = 0
        while num:
            section = num % 1000
            parse(section, suffix_index)
            num //= 1000
            suffix_index += 1

        return " ".join(self.ans)
