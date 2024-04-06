# Sorts

## Bucket Sort

Idea is to sort values into a bucket which represents a range of values. This dramatically decreases the number of comparisons or iterations required. This is typically useful when trying to find two numbers that satisfy some set of constraints.

Template:
1. Identify the Range: Determine the range of the input elements. This is important because you'll need to create buckets that can cover the entire range of the values.
2. Create Buckets: Based on the range and the number of buckets you decide to create (often proportional to the number of elements), initialize the buckets. Buckets can be arrays, lists, or any other collection.
3. Distribute Elements into Buckets: Iterate over the input array, placing each element into the appropriate bucket. The bucket is typically chosen based on the element's value in relation to the overall range.
4. Sort Buckets: Individually sort the elements within each bucket. This can be done using any sorting algorithm, but often, a simple algorithm like insertion sort is used because buckets typically contain a small number of elements.

For an MD (Markdown) file, you can present the formula using a combination of text and code blocks for clarity. Here's how you could structure it:

---

**Optimal Gap in Bucket Sort:**

- **Uniform Gap Scenario:** In an ideal case for bucket sort, elements in the array are evenly distributed with a uniform gap between adjacent elements.

- **Gap Calculation:** For \(n\) elements, the uniform gap (\(t\)) between any two adjacent elements is calculated as follows:

  ```
  t = (max - min) / (n - 1)
  ```

  Where `max` and `min` are the maximum and minimum values in the array, respectively.

- **Significance:** This uniform gap represents the optimal distance between elements, guiding the ideal bucket range or size in bucket sort. It ensures that the sorting within each bucket is as efficient as possible by minimizing the work needed to sort elements within buckets.

---

This format should integrate well into most Markdown viewers, providing a clear and concise explanation along with an easy-to-understand formula representation.

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

[Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)

```python
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        buckets: List[List[str]] = [[] for _ in range(max_freq + 1)]
        for c, freq in counts.items():
            buckets[freq].append(c)

        result = []
        for freq, c_list in enumerate(buckets):
            for c in c_list:
                result.append(c * freq)
        return "".join(result[::-1])

```

[Sort an Array](https://leetcode.com/problems/sort-an-array/)

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_val, min_val = max(nums), min(nums)
        buckets_size = abs(max_val - min_val)
        offset = min_val
        buckets = [0] * (buckets_size + 1)
        for num in nums:
            buckets[num - offset] += 1

        result = []
        for num, freq in enumerate(buckets):
            if freq:
                result.extend([num + offset] * freq)
        return result
```
OR
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            # Find the minimum and maximum values in the array.
            minVal, maxVal = min(nums), max(nums)
            counts = Counter(nums)

            index = 0
            # Place each element in its correct position in the array.
            for val in range(minVal, maxVal + 1, 1):
                # Append all 'val's together if they exist.
                while counts.get(val, 0) > 0:
                    nums[index] = val
                    index += 1
                    counts[val] -= 1

        counting_sort()
        return nums
```

Here I create a bucket for each possible number in a range between the max and the min values provided. Then increment how many of each occur in the input. After which I loop through the buckets extending the result set. This could also be considered *Counting* sort.

In this example I create a bucket for each frequency.

[Maximum Gap](https://leetcode.com/problems/maximum-gap)

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_val, min_val = max(nums), min(nums)
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))
        num_of_buckets = (max_val - min_val) // bucket_size + 1
        bucket_min = [float("inf")] * num_of_buckets
        bucket_max = [float("-inf")] * num_of_buckets

        for num in nums:
            bucket_idx = (num - min_val) // bucket_size
            bucket_min[bucket_idx] = min(bucket_min[bucket_idx], num)
            bucket_max[bucket_idx] = max(bucket_max[bucket_idx], num)

        prev_bucket_max = min_val
        max_gap = 0
        for i in range(num_of_buckets):
            if bucket_min[i] == float("inf") and bucket_max[i] == float("-inf"):
                continue

            max_gap = max(max_gap, bucket_min[i] - prev_bucket_max)
            prev_bucket_max = bucket_max[i]

        return max_gap
```

[Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words)

```python
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)
        buckets: List[List[str]] = [[] for _ in range(max(counts.values()) + 1)]

        for word, count in counts.items():
            buckets[count].append(word)

        result: List[str] = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                buckets[i].sort()
                result.extend(buckets[i][: k - len(result)])
            if len(result) >= k:
                break
        return result[:k]
```

# Cycle Sort

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

# Radix Sort

Template:
1. Identify the Maximum Number: Find the maximum number in the array to know the maximum number of digits any number has.
2. Sorting by Individual Digits: Starting from the least significant digit (LSD) to the most significant digit (MSD), sort the numbers based on the current digit. This can be done using a stable sort like counting sort for each digit.
3. Loop through Digits: For each digit, distribute the elements into buckets (0-9 for decimal numbers) based on the current digit. After distributing, collect the items from the buckets back into the array. Repeat this for each digit, moving to the next more significant digit each time.
4. Concatenate Results: After sorting by each digit, the array will be sorted. There's no need to concatenate buckets as in bucket sort since the array is modified in-place.


