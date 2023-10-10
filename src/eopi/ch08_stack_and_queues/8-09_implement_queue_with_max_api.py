""" Implement Queue with Max API """

from collections import namedtuple

Element = namedtuple('Element', ['value', 'prev_max'])
class MaxQueue:

    def __init__(self) -> None:
        self.elements = []
        self.max_seen = float('-inf')

    def enqueue(self, x) -> None:
        self.elements.append(Element(x, self.max_seen))
        self.max_seen = max(self.max_seen, x)

    def dequeue(self) -> int:
        if not self.elements:
            return -1
        removed = self.elements.pop()
        self.max_seen = removed.prev_max
        return removed.value

    def max(self) -> int:
        return self.max_seen

queue = MaxQueue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.max())
print(queue.dequeue())
print(queue.max())
