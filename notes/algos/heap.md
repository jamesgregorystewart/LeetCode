# Heaps

Heaps are useful for problems specifying the need to find the kth largest or smallest element or elements in some collection.

In python there is no built in Balance Binary Search Tree (BBST) so we can mimick that with use of a counter and some intelligent variable management.

Finding the kth smallest number among M contiguous numbers in an array of size N.
```python
import heapq
from collections import Counter

def find_kth_smallest(nums, k, m):
    # Initial window heap and counter for elements to be lazily removed
    window = nums[:m]
    heapq.heapify(window)
    to_be_removed = Counter()
    
    result = []
    for i in range(m, len(nums) + 1):
        # Add the current window's kth smallest to the result
        # Adjust for the elements that are in the heap but should be ignored
        count = 0
        heap_store = []
        while window and count < k:
            smallest = heapq.heappop(window)
            heap_store.append(smallest)
            if to_be_removed[smallest]:
                to_be_removed[smallest] -= 1
                continue
            count += 1
            if count == k:
                result.append(smallest)
        while heap_store:
            heapq.heappush(window, heap_store.pop())
        
        if i == len(nums):
            break
        
        # Slide the window: remove the oldest, add the newest
        out_elem = nums[i-m]
        in_elem = nums[i]
        to_be_removed[out_elem] += 1
        heapq.heappush(window, in_elem)
    
    return result

# Example usage
nums = [1, 3, 5, 2, 8, 7, 6, 4]
k = 2
m = 3
print(find_kth_smallest(nums, k, m))
```

[Max Sliding Window](https://leetcode.com/problems/sliding-window-maximum/)

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        max_heap = [num * -1 for num in nums[:k]]
        heapq.heapify(max_heap)
        removed = defaultdict(int)

        n = len(nums)
        result = []
        for i in range(k, n + 1):
            while (max_val := -max_heap[0]) in removed and removed[max_val]:
                removed[max_val] -= 1
                heapq.heappop(max_heap)
                continue
            result.append(max_val)

            if i == n:
                break

            removed[nums[i - k]] += 1
            heapq.heappush(max_heap, nums[i] * -1)
        return result
```

This was overkill because I only needed to find the max in a range, thus a monotonic stack would be more efficient; nonetheless good practice for a heap


[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums 

        counts = Counter(nums)
        return heapq.nlargest(k, counts.keys(), key=counts.get)
```
