from math import ceil, floor
import re


class Solution:
    def calculate(self, s: str) -> int:

        operators = {
            "+": lambda y, x: x + y,
            "-": lambda y, x: x - y,
            "*": lambda y, x: x * y,
            "/": lambda y, x: (
                floor(x / y) if (x > 0 and y > 0) or (x < 0 and y < 0) else ceil(x / y)
            ),
        }

        # get rid of spaces
        s.replace(" ", "")

        def get_num(i, direction):
            j = i
            while j >= 0 and j < len(s) and s[j].isdigit():
                j += direction
            start, end = (i, j) if i < j else (j, i)
            return start, end, int(s[start : end + 1])

        next_s = ""
        i = 0
        while i < len(s):
            if s[i] in ["*", "/"]:
                x_start, _, x = get_num(i - 1, -1)
                _, y_end, y = get_num(i + 1, 1)
                result = operators[s[i]](y, x)
                next_s = next_s[:x_start]
                next_s += str(result)
                i = y_end
            i += 1
        print(next_s)

        while next_s:
            i = 0
            while i < len(next_s) and next_s[i].isdigit():
                i += 1
            if i == len(next_s):
                return int(next_s)
            j = i + 1
            while j < len(next_s) and next_s[j].isdigit():
                j += 1

            x = int(next_s[:i])
            y = int(next_s[i + 1 : j + 1])
            result = operators[next_s[i]](y, x)
            next_s = result + next_s[j + 1 :]
