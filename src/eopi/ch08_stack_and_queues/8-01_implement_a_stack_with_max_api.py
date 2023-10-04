""" Implement a Stack with Max API """

from typing import List, Tuple

class MaxStack:
    def __init__(self):
        self.nums: List(Tuple(int, int)) = []
        self.max_prev = -1

    def push(self, val: int) -> None:
        if len(self.nums) == 0:
            self.nums.append((val, 0))
            self.max_prev = 0
        else:
            self.nums.append((val, self.max_prev))
            if val > self.nums[self.max_prev][0]:
                self.max_prev = len(self.nums)-1

    def pop(self) -> int:
        self.max_prev = self.nums[-1][1]
        return self.nums.pop(-1)[0]
        
            
    def get_max(self) -> int:
        return self.nums[self.max_prev][0]


max_stack = MaxStack()
max_stack.push(0)
max_stack.push(3)
max_stack.push(2)
max_stack.push(5)
max_stack.push(4)
print(max_stack.get_max())
print(max_stack.pop())
print(max_stack.get_max())
print(max_stack.pop())
print(max_stack.get_max())
