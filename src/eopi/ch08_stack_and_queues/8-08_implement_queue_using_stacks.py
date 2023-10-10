""" Implement Queue Using Stacks """

from typing import List

class StackedQueue:
    
    def __init__(self) -> None:
        self.enq = []
        self.deq = []

    def enqueue(self, x: int) -> None:
        self.enq.append(x)

    def dequeue(self) -> int:
        if self.deq:
            return self.deq.pop()
        while self.enq:
            self.deq.append(self.enq.pop())
        return self.deq.pop()


queue = StackedQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
queue.enqueue(4)
print(queue.dequeue())

