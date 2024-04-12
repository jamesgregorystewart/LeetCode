from typing import List

# My solution
# class Solution:
#     def addOperators(self, num: str, target: int) -> List[str]:
#         def dfs(expression: List[str], i) -> None:
#             if i == len(num) - 1:
#                 expression.append(num[i])
#                 stringified = "".join(expression)
#                 if eval(stringified) == target:
#                     self.ans.append(stringified)
#                 expression.pop()
#                 return
#
#             expression.append(num[i])
#             for op in self.operators:
#                 if op:
#                     expression.append(op)
#                 if not op and num[i] == "0":
#                     expression.pop()
#                     return
#                 dfs(expression, i + 1)
#                 if op:
#                     expression.pop()
#             expression.pop()
#
#         self.operators = ["+", "-", "*", None]
#         self.ans = []
#         dfs([], 0)
#         return self.ans


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(index, path, value, last):
            # If we've reached the end of `num` and the current value equals the target
            if index == len(num) and value == target:
                ans.append("".join(path))
                return

            for i in range(index, len(num)):
                # Avoid numbers with leading zeros
                if i > index and num[index] == "0":
                    break

                # Slice the current part of the string
                cur_str = num[index : i + 1]
                cur = int(cur_str)

                # If it's the start of the path, we just add the number
                if index == 0:
                    dfs(i + 1, path + [cur_str], cur, cur)
                else:
                    # Addition
                    dfs(i + 1, path + ["+", cur_str], value + cur, cur)
                    # Subtraction
                    dfs(i + 1, path + ["-", cur_str], value - cur, -cur)
                    # Multiplication
                    dfs(
                        i + 1,
                        path + ["*", cur_str],
                        value - last + last * cur,
                        last * cur,
                    )

        ans = []
        dfs(0, [], 0, 0)
        return ans


# Example usage
sol = Solution()
print(sol.addOperators("105", 5))
