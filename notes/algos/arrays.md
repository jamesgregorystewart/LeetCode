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

# Sliding Window

Sliding window is not applicable when the values of an array are negative and positive, because there is no longer a heuristic to move the pointers left or right. In this case, you must iterate through all the values and leverage datastructures to optimize.

# Prefix Sums

### Prefix Sums: Summary

Prefix sums are a powerful technique in algorithmic problem solving, particularly useful for efficiently answering queries about the sum of elements in a subrange of an array. This technique involves precomputing cumulative sums of an array, allowing for the quick calculation of the sum of any contiguous segment of the array.

#### Intuition:

The core idea behind prefix sums is to store the sum of elements from the start of the array up to each index. This enables you to calculate the sum of a range in constant time, after an initial linear time preprocessing step.

#### When to Use Them:

- **Subarray Sums**: When you need to frequently calculate the sum of subarrays.
- **Queries**: In scenarios where you have multiple queries asking for the sum of different subranges, and you want to avoid recalculating sums from scratch.
- **Difference Arrays**: Prefix sums can be used in reverse to construct an array from its differences. This is useful in range update queries in mutable arrays.
- **Counting Subarrays with a Given Sum**: Can be used in combination with hashing to count subarrays that sum to a specific value.
- **2D Prefix Sums**: For 2D arrays, when you need to calculate the sum of elements within a submatrix repeatedly.

#### Template for 1D Prefix Sums:

```python
# Preprocess to generate prefix sums
def prefix_sums(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix

# Calculate sum of the subarray arr[i:j] (inclusive of i, exclusive of j)
def range_sum(prefix, i, j):
    return prefix[j] - prefix[i]
```

#### Intuition and Analysis:

The main advantage of prefix sums is reducing the time complexity of sum queries from O(n) to O(1) after an O(n) preprocessing time. The space complexity is O(n) for storing the prefix sums.

- **Intuition**: By storing cumulative sums up to each index, you effectively cache the result of all possible sum queries, allowing for quick calculations later.
- **Analysis**: The use of additional space (for the prefix array) trades off for significant savings in time, especially in scenarios with multiple queries.

#### Advanced Use Cases:

- **Multi-dimensional Prefix Sums**: For 2D grids or matrices, prefix sums can be extended to quickly calculate the sum of any submatrix. This involves creating a 2D prefix sum array where each entry (i,j) stores the sum of elements in the rectangle defined by (0,0) to (i,j).
- **Difference Array Technique**: Sometimes, it's easier to apply updates to a difference array and then use prefix sums to reconstruct the actual values. This is especially useful for range updates and queries in mutable arrays.

### Conclusion:

Prefix sums are a versatile tool that can significantly optimize the performance of algorithms that involve sum queries over arrays. By preprocessing an array into its prefix sums, you turn potentially expensive operations into constant-time lookups, making it a go-to technique for a wide range of problems.

[Subarray Sum Equals k](https://leetcode.com/problems/subarray-sum-equals-k)

```python
def subarraySum(nums, k):
    count, currentSum = 0, 0
    map = {0: 1}  # Initialize with sum 0 to handle edge cases

    for num in nums:
        currentSum += num  # Update cumulative sum
        # If currentSum - k exists in map, it means there's a subarray ending here with sum k
        count += map.get(currentSum - k, 0)
        # Update map with the current sum's new frequency
        map[currentSum] = map.get(currentSum, 0) + 1

    return count
```
