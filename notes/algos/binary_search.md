# Binary Search

## Template I 

```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
```

In reality, problems are going to be prompted such that you need to do some modified version of this. For e.g.:

[Search in Rotated Sorted Array](https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:
                # left side is sorted
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right side is sorted
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

## Template II

This template is most useful when there isn't a *target* against we can compare and terminate. Instead the answer is relative to its neighbors and we will need to check mid against other elements. These other elements could be the the element at left, the element at right, or possibly even adjacent.

```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    # Post-processing:
    # End Condition: left == right
    if nums[left] == target:
        return left
    return -1
```

- Advanced way to implement Binary Search
- Use mid's right neighbor to determine if the condition is met and decide whether to go left or right
- Guarantees Search Space is at least 2 in size at each step
- Post-proicessing required. Loop/Recursion ends when you have 1 element left. Need to assess assessif the remaining element meets the condition.

This is useful for if your qualifying condition is to check two adjacent elements and you are checking the element to the right of mid at each step

[First Bad Version](https://leetcode.com/problems/first-bad-version/description/)
```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

```

Here we need to find the first version that is bad, and we don't want to check mid + 1 for a bad one, or mid-1 for a good one, because this can lead to index errors. Instead, we manage left and right so that the loop will terminate when left == right and left and right is the answer.

[Find Peak Element](https://leetcode.com/problems/find-peak-element/)
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
```

Here using the second template saves us some complexity. Instead of having to check both left and right adjacent elements to mid to determine if we are a peak, we just check the right side, and we will exit at a peak.

## Template III

```python
def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid

    # Post-processing:
    # End Condition: left + 1 == right
    if nums[left] == target: return left
    if nums[right] == target: return right
    return -1
```

- Use mid's neighbors to determine if the condition is met and decide whether to go left or right
- Guarantees Search Space is at least 3 in size at each step
- Post-processing required. Loop/Recursion ends when you ahve 2 elements left. Need to assess if the remaining elements meet the condition


## Interesting Examples

[Nth Digit](https://leetcode.com/problems/nth-digit/description/)
```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = base = 1
        while n > 9 * base * digit:
            n -= 9 * base * digit
            digit += 1
            base *= 10
        q, r = divmod(n - 1, digit)
        return int(str(base + q)[r])
```

The intuition for this problem comes from the fact there are
1-9 -- 9 numbers and 9 digits
10-99 -- 90 numbers and 180 digits
100-999 -- 900 numbers and 2700 digits

so we can use this pattern to logarithmically find the first number with the base for which we are searching, then divide the number of digits from that start and find the ith word from there and then use a remainder to find the index of the digit in the word we know has the answer.


[Find Right Interval](https://leetcode.com/problems/find-right-interval/description/)
```python
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted(
            [[start, i] for i, (start, _) in enumerate(intervals)]
            + [[float("inf"), -1]]
        )
        return [
            sorted_intervals[bisect.bisect_left(sorted_intervals, [end, 0])][1]
            for _, end in intervals
        ]
```

Here we use list comprehensions to first, create the a list with the sorted starts and their initial indices, and second, to return a list of the original index of each interval whose start is greater than or equal to the end of each interval in intervals. We will use binary search to find the index to the interval with the smallest start value greater than or equal to the current interval's end value.
