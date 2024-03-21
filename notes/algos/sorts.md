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
