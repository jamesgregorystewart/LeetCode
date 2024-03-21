# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
#
#
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
#
# Constraints:
#
# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].

from typing import List, Tuple
import heapq
from collections import Counter

# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         task_counts = Counter(tasks)
#         max_heap_a, max_heap_b = [-value for key, value in task_counts.items()], []
#         heapq.heapify(max_heap_a)
#
#         res = 0
#         while max_heap_a or max_heap_b:
#             iterations = 0
#             if max_heap_a:
#                 while max_heap_a:
#                     if iterations <= n:
#                         task = heapq.heappop(max_heap_a)
#                         task += 1
#                         if task != 0:
#                             heapq.heappush(max_heap_b, task)
#                         iterations += 1
#                     else:
#                         heapq.heappush(max_heap_b, heapq.heappop(max_heap_a))
#             else:
#                 while max_heap_b:
#                     if iterations <= n:
#                         task = heapq.heappop(max_heap_b)
#                         task += 1
#                         if task != 0:
#                             heapq.heappush(max_heap_a, task)
#                         iterations += 1
#                     else:
#                         heapq.heappush(max_heap_a, heapq.heappop(max_heap_b))
#             if not max_heap_a and not max_heap_b:
#                 res += iterations
#             else:
#                 res += n + 1
#
#         return res


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(max_heap)
        storage: List[Tuple[int, str]] = []
        ans = 0
        while max_heap:
            for _ in range(n + 1):
                if not max_heap and not storage:
                    return ans
                ans += 1
                if not max_heap and storage:
                    continue
                task = heapq.heappop(max_heap)
                if task[0] == -1:
                    continue
                storage.append((task[0] + 1, task[1]))
            while storage:
                heapq.heappush(max_heap, storage.pop())
        return ans


solution = Solution()
print(
    solution.leastInterval(
        tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2
    )
)
print(solution.leastInterval(["A", "A", "A", "B", "B", "B"], n=2))
print(solution.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0))
