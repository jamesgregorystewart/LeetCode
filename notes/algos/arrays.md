# Arrays

# Monotonic Deque

[Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum)

Monotonic Deque implementation
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i in range(len(nums)):
            # maintain the largest element in q in leftmost position
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

            if q and q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                result.append(nums[q[0]])

        return result
```

A monotonic deque is a data structure that supports operations similar to a regular double-ended queue (deque) but maintains its elements in either entirely non-increasing or non-decreasing order. This property is particularly useful in problems requiring efficient minimum or maximum queries over sliding windows or subsequences of a sequence of values.

### How it Works

- **Monotonic Increasing Deque**: Ensures that elements in the deque are in non-decreasing order from the front to the back. This is useful for finding minimum values over a range.
- **Monotonic Decreasing Deque**: Ensures that elements in the deque are in non-increasing order from the front to the back. This is ideal for finding maximum values over a range.

When a new element is added, the deque removes elements from the back (for an increasing deque) or the front (for a decreasing deque) that are worse than the new element according to the order property it maintains (e.g., higher values in an increasing deque, or lower values in a decreasing deque). This ensures that the best candidate (minimum or maximum) always remains accessible at one end of the deque.

### When to Use a Monotonic Deque

1. **Sliding Window Problems**: Especially when you're asked to find the minimum or maximum value in a sliding window as it moves across an array. A monotonic deque allows you to add new elements from one end and remove outdated elements from the other end efficiently while maintaining the desired order.

2. **Problems Requiring Quick Maximum/Minimum Queries**: Any time you need to quickly query the maximum or minimum value from a set of recent values, and the set is updated in a way where only the newest value or the oldest value is changed at any time.

### Recognition Signals

- The problem involves a sliding window, and you need to compute some form of cumulative statistic (e.g., max, min) within the window as it moves.
- The problem states or implies a need for efficient retrieval of maximum or minimum elements from a subset of elements that gets updated sequentially.
- Dynamic programming problems where the state transition depends on the maximum or minimum of previous states within a certain range.

### Example

A classic problem where a monotonic deque shines is the "Sliding Window Maximum" (e.g., LeetCode 239). Here, you're given an array `nums` and an integer `k`, and you need to find the maximum value in each sliding window of size `k` as it moves from left to right across the array. A monotonic decreasing deque can be used to keep track of potential candidates for the maximum value in the current window, ensuring O(1) time complexity for querying the maximum and O(n) overall time complexity for processing the entire array, where `n` is the number of elements in `nums`.

### Conclusion

Understanding when and how to apply a monotonic deque can significantly simplify the solution to complex problems, especially those involving sliding windows or sequences where maintaining a running maximum or minimum is crucial. Recognizing the potential for its application often comes down to identifying patterns in problems where elements are processed sequentially and efficient min/max queries are essential for the solution.
