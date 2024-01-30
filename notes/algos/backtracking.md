# Backtracking

When solving a backtracking problem. You will typically use recursion to try out the different inputs or paths and fallback to try other inputs or paths from a previous state. It involves choosing an option, trying to build a solution incrementally, and abandoning this path (backtracking) as soon as it determines that this path cannot possibly lead to a complete solution.

Although a breadth-first search could also be used to enumerate sollutions, a depth-first search is greatly preferred because it uses much less space. The current state of a search is completely represented by the pathh form the root to the current search depth-first node. This requires space proportional to the hieght of the tree. In breadth-first search, the searchqueue stores all the nodes at the curernt level, which which is proportional to the width of the search tree.

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

Problem: [N Queens](https://leetcode.com/problems/n-queens/description/)
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(x, queens, config):
            if len(config) == n:
                ans.append(config)
                return
            for i in range(n):
                if safe((x, i), queens):
                    row = "." * n
                    row = row[:i] + "Q" + row[i + 1 :]
                    backtrack(x + 1, queens + [(x, i)], config + [row])

        def safe(position, queens) -> bool:
            for queen in queens:
                """
                Two points are diagonal to each other if the abs diff of in the x-coords
                and y-coords are equivalent. This is because in a plane, a diagonal
                in a square or a rectangle has equal horizontal and vertical distances
                """
                if position[1] == queen[1] or abs(position[0] - queen[0]) == abs(
                    position[1] - queen[1]
                ):
                    return False
            return True

        ans: List[List[str]] = []
        backtrack(0, [], [])
        return ans
```
