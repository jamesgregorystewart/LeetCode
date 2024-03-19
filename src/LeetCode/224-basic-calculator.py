from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        parts: List[List[str]] = []
        cur_part: List[str] = []
        operators = {
            "+": lambda x, y: int(x) + int(y),
            "-": lambda x, y: int(x) - int(y),
        }
        index = 0
        while index < len(s):
            if s[index] == "(" and cur_part:
                # start a new segment
                parts.append(cur_part)
                cur_part = []
            elif s[index].isdigit():
                # identify and append multi digit number
                end = index
                while end < len(s) - 1 and s[end + 1].isdigit():
                    end += 1
                cur_part.append(s[index : end + 1])
                index = end
            elif s[index] in ["+", "-"]:
                cur_part.append(s[index])
            if s[index] == ")" or index == len(s) - 1:
                # evaluate segment
                for i in range(0, len(cur_part) - 1, 2):
                    operand1, operator, operand2 = (
                        cur_part[i],
                        cur_part[i + 1],
                        cur_part[i + 2],
                    )
                    res = str(operators[operator](operand1, operand2))
                    cur_part[i + 2] = res
                if not parts:
                    parts.append([cur_part[-1]])
                else:
                    parts[-1].append(cur_part[-1])
            index += 1
        print(parts)
        return int(parts[-1][-1])


solution = Solution()
print(solution.calculate("1 + 1"))
print(solution.calculate("2-1 + 2"))
print(solution.calculate("(2-1 + 2)"))
print(solution.calculate("1+(2-1 + 2)"))
