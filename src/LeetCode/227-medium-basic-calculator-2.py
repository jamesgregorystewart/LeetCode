from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        num = 0
        operand, operator = None, None
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y,
        }
        for c in s:
            if c == " ":
                continue
            elif c.isdigit():
                num *= 10
                num += int(c)
            else:
                if operand is not None:
                    stack.append(operators[operator](operand, num))
                    operand, operator = None, None
                else:
                    stack.append(num)
                if c in ["+", "-"]:
                    stack.append(c)
                elif c in ["*", "/"]:
                    operand = stack.pop()
                    operator = c

                num = 0

        if operand is not None:
            stack.append(operators[operator](operand, num))
        elif not stack or not stack[-1][-1].isdigit():
            stack.append(num)

        # Evaluate + and -
        while stack:
            if len(stack) == 1:
                return stack.pop()
            op1, operator, op2 = stack.popleft(), stack.popleft(), stack.popleft()
            stack.appendleft(operators[operator](op1, op2))
