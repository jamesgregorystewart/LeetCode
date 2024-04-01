# Sorts

## Bucket Sort

Idea is to sort values into a bucket which represents a range of values. This dramatically decreases the number of comparisons or iterations required. This is typically useful when trying to find two numbers that satisfy some set of constraints.

Problem: [Contains Duplicate III](https://leetcode.com/problems/contains-duplicate-iii/description/)
```python
class Solution:
  def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    if not nums or indexDiff <= 0 or valueDiff < 0:
      return False

    mini = min(nums)
    diff = valueDiff + 1  # In case of valueDiff = 0
    bucket = {}

    def getKey(num: int) -> int:
        # Scale value down to a bucket id which scales linearly as values increase
      return (num - mini) // diff

    for i, num in enumerate(nums):
      key = getKey(num)
      if key in bucket:  # Current bucket
        # there is for certain a value within the value range to satisfy constraints
        return True
      # Left adjacent bucket
      if key - 1 in bucket and num - bucket[key - 1] < diff:
        return True
      # Right adjacent bucket
      if key + 1 in bucket and bucket[key + 1] - num < diff:
        return True
      bucket[key] = num
      if i >= indexDiff:
        del bucket[getKey(nums[i - indexDiff])]

    return False
```

## Cycle Sort

Cycle Sort is a sorting algorithm that can sort a given sequence in a range from a to n by putting each element at the index that corresonds to its value.

In the below problem we can leverage this sorting technique and then returning the first index i+1 where nums[i] != i+1.

[First Missing Positive](https://leetcode.com/problems/first-missing-positive/)

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] < n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i, num in enumerate(nums):
            if i + 1 != num:
                return i + 1

        return n + 1
```

