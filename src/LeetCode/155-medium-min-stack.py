from typing import List, Tuple


class MinStack:
    def __init__(self):
        self.stack: List[Tuple[int, int]] = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, 0))
        else:
            min_i = self.stack[-1][1]
            n = len(self.stack)
            new_i = n if val < self.stack[min_i][0] else min_i
            self.stack.append((val, new_i))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[self.stack[-1][1]][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
