# Dynamic Programming

## Top-Down vs Bottom-Up

1. Bottom-up, AKA Tabulation
2. Top-Down AKA Memoization

## Bottom-Up

```python
F = array of length (n + 1)
F[0] = 0
F[1] = 1
for i from 2 to n:
    F[i] = F[i - 1] + F[i - 2]
```

This is typically faster, uses less space, and is iterative

## Top-Down
```python
memo = hashmap
Function F(integer i):
    if i is 0 or 1: 
        return i
    if i doesn't exist in memo:
        memo[i] = F(i - 1) + F(i - 2)
    return memo[i]
```

This is usually simpler, and easier to write. Typically this is a good place to start.

## Characteristics of DP Problems

DP problems will typically ask for the optimum value of something, or the number of ways to do something.
- What is the minimum cost of doing...
- What is the max profit from...
- How many ways are there to...
- What is the longest possible...
- Is it possible to reach a certain point...

Second characteristic of DP problems is that future "decisions" depend on earlier decisions. You must factor in results from previous decisions.

## Framework for DP Problems

1. A function or data structure that will compute/contain the answer to the problem for every given state.
2. A recurence relation to transition between states.
3. Base cases, so that our recurrence relation  doesn't go on infinitely.

## Examples

### Basic Top-Down

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i): 
            """A function that returns the answer to the problem for a given state."""
            # Base cases: when i is less than 3 there are i ways to reach the ith stair.
            if i <= 2: 
                return i
            
            # If i is not a base case, then use the recurrence relation.
            return dp(i - 1) + dp(i - 2)
        
        return dp(n)
```

### Memoized Top-Down

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i):
            if i <= 2: 
                return i
            if i not in memo:
                # Instead of just returning dp(i - 1) + dp(i - 2), calculate it once and then
                # store the result inside a hashmap to refer to in the future.
                memo[i] = dp(i - 1) + dp(i - 2)
            
            return memo[i]
        
        memo = {}
        return dp(n)
```

### Bottom-Up

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
            
        # An array that represents the answer to the problem for a given state
        dp = [0] * (n + 1)
        dp[1] = 1 # Base cases
        dp[2] = 2 # Base cases
        
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] # Recurrence relation

        return dp[n]
```

## Converting Top-Down to Bottom-Up

When a problem is most easily solved with a top-down solution, complete that solution and then follow-up by making it iterative / bottom-up. This process make look like this:

1. Start with Top-Down Solution
```python
class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(i: int) -> int:
            # Base cases
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo:
                # Use recurrence relation to calculate dp[i].
                memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
            
            return memo[i]
        
        memo = {}
        return dp(len(nums) - 1)
```
2. Initialize an array dp according to our state variables. Here our state variable is *i* and can hold *n* values.
```python
class Solution:
    def rob(self, nums: List[int]) -> int:        
        n = len(nums)
        dp = [0] * n
        
        return dp[n - 1]
```
3. Set the Base Cases
``` python
class Solution:
    def rob(self, nums: List[int]) -> int:   
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        
        #Base Cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        return dp[n - 1]
```
4. Write for-loop to iterate over the state variables, starting from base cases
```python
class Solution:
    def rob(self, nums: List[int]) -> int:   
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        
        #Base Cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            pass
        
        return dp[n - 1]
```
5. Lastly, copy the recurrence relation over from the top-down solution and put it in the for-loop. Return dp[n-1].
```python
class Solution:
    def rob(self, nums: List[int]) -> int:   
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        
        #Base Cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            # Use recurrence relation to calculate dp[i].
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[n - 1]
```

## Iteration in Recurrence Relation

Problems may state that you can take up to *k* steps at a time in which case you must iterate k times and take this into account in your recurrence relation. Your static relation such as `dp(i)=min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])` may become `dp(i)=min(dp(j) + cost[j]) for all (i - k) <= j < i`

## Kadane's Algorithm

Kadane's Algorithm is an algorithm that can find the maximum sum subarray given an array of numbers in O(n) time and O(1) space. This algorithm involves iterating through the array using an integer variable *current* and at each index *i*, determines if elements before index i are "worth" keeping, or if they should be "discarded". The algorithm is only useful when the array can contain negative numbers. If *current* becomes negative, it is reset, and we start considering a new subarray starting at the current index.

Pseudocode for the algorithm:
```python
// Given an input array of numbers "nums",
1. best = negative infinity
2. current = 0
3. for num in nums:
    3.1. current = Max(current + num, num)
    3.2. best = Max(best, current)

4. return best
```
Line *3.1* is where the magic happens. If current has become less than 0 from including too many or too large negative numbers, the algorithm "throws it away" and resets.


## Examples

[Find the Sum of Subsequence Powers](https://leetcode.com/problems/find-the-sum-of-subsequence-powers)

```python
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = 0

        @lru_cache(None)
        def dp(idx, min_diff, last_choose, left_k):
            if left_k == 0:
                if min_diff != float("inf"):
                    return min_diff
                else:
                    return 0
            if idx == len(nums):
                return 0
            choose = dp(
                idx + 1,
                min(min_diff, abs(last_choose - nums[idx])),
                nums[idx],
                left_k - 1,
            )
            not_choose = dp(idx + 1, min_diff, last_choose, left_k)
            return (choose + not_choose) % MOD

        return dp(0, float("inf"), float("inf"), k)
```
