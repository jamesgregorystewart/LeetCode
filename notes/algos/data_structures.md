# Data Structures

This doc serves as a place for a general overview of data structures, their uses, pros and cons, as well as the use cases they serve best.

## Sorting K values N times

Occasionally you will have an array, string, or other input which requires iterative review to build a result of a list or aggregation. Occasionally that sort of iterative analysis with sorting can be solved best with a heap or tree. `heapq` is the module for heaps in python and `sortedcontainers` has a class called `SortedList` which is implemented as a balanced search tree of lists that offers `O(log(N))` search, add, and remove. A Heap can offer similar benefits however arbitrary searching is O(N) and arbitrary removal is O(N) as well.

### Problem using `SortedList`
[Sliding Window Median](https://leetcode.com/problems/sliding-window-median/description/)

```python
from sortedcontainers import SortedList
#O(N* log(K)); With a heap this would have been O(N*Klog(K))
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        tree = SortedList()
        res: List[float] = []
        for i, num in enumerate(nums):
            tree.add(num)
            if len(tree) > k:
                tree.remove(
                    nums[i - k]
                )  # if this was a heap it would be O(k); this is log(K)
            if len(tree) == k:
                median = (
                    tree[k // 2] if k % 2 else (tree[k // 2 - 1] + tree[k // 2]) / 2
                )
                res.append(float(median))
        return res
```
