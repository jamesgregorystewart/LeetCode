"""
stack = []
pq: List[item] = max_heap
class item
map: Dict[val, item] = {}

"""

import heapq


# class Item:
#     def __init__(self, val, index) -> None:
#         self.val = val
#         self.count = 1
#         self.index = [index]
#
#     def __lt__(self, other) -> bool:
#         if self.count != other.count:
#             return self.count > other.count
#         return self.index[-1] > other.index[-1]
#
#     def __repr__(self) -> str:
#         return "val: {}; count: {}; indices: {}".format(
#             self.val, self.count, self.index
#         )
#
#
# class FreqStack:
#
#     def __init__(self):
#         self.index = 0
#         self.pq = []
#         self.map = {}
#
#     def push(self, val: int) -> None:
#         if val in self.map:
#             item = self.map[val]
#             item.count += 1
#             item.index.append(self.index)
#             self.index += 1
#             heapq.heapify(self.pq)
#         else:
#             item = Item(val, self.index)
#             self.map[val] = item
#             heapq.heappush(self.pq, item)
#             self.index += 1
#
#     def pop(self) -> int:
#         item = heapq.heappop(self.pq)
#         if item.count > 1:
#             item.count -= 1
#             item.index.pop()
#             heapq.heappush(self.pq, item)
#         else:
#             del self.map[item.val]
#
#         return item.val


class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        self.freq[x] += 1
        self.maxfreq = max(self.maxfreq, self.freq[x])
        self.group[self.freq[x]].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
