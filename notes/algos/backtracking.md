# Backtracking

When solving a backtracking problem. You will typically use recursion to try out the different inputs or paths and fallback to try other inputs or paths from a previous state. It involves choosing an option, trying to build a solution incrementally, and abandoning this path (backtracking) as soon as it determines that this path cannot possibly lead to a complete solution.

Problem Types: Common backtracking problems include puzzles, combinatorial problems (like permutations, combinations, n-queens), and partitioning problems (like subset sum, palindromic partitions)

Optimizations to look for:
- Sorting inputs    
- Early Termination

A generic backtracking function often follows this structure:
```python
def backtrack(path, choices):
    if goal_reached(path):
        add_solution(path)
        return
    for choice in choices:
        if is_valid_choice(choice, path):
            make_choice(choice, path)
            backtrack(path, updated_choices)
            undo_choice(choice, path)
```

Classic Examples:

Problem [Combination Sum](https://leetcode.com/problems/combination-sum/description/)

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(sum_set, index, cur_sum) -> None:
            if cur_sum == target:
                results.append(sum_set.copy())
            elif cur_sum > target:
                return
            else:
                for i in range(index, len(candidates)):
                    if cur_sum + candidates[i] <= target:
                        backtrack(sum_set + [candidates[i]], i, cur_sum + candidates[i])

        results: List[List[int]] = []
        backtrack([], 0, 0)
        return results
```

Problem: [Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/)
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(i, cur):
            if i == len(s):
                ans.append(cur.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i : j + 1]):
                    cur.append(s[i : j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()

        def is_palindrome(t: str) -> bool:
            n = math.ceil(len(t) / 2)
            return t[:n] == t[-n:][::-1]

        ans: List[List[str]] = []
        backtrack(0, [])
        return ans
```
