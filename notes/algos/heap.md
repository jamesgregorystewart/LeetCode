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
        while count < k:
            smallest = heapq.heappop(window)
            if to_be_removed[smallest]:
                to_be_removed[smallest] -= 1
                continue
            count += 1
            if count == k:
                result.append(smallest)
            heapq.heappush(window, smallest)
        
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
