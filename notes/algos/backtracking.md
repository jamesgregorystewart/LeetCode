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
``

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

[Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number)

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path) -> None:
            if index == len(digits):
                combinations.append("".join(path))
                return

            for letter in letters[digits[index]]:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()

        combinations = []
        backtrack(0, [])
        return combinations
```


[Combinations](https://leetcode.com/problems/combinations/)

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(i, combo) -> None:
            if len(combo) == k:
                combinations.append(combo[:]) # combo[:] returns a shallow copy here
                return

            for num in range(i, n + 1):
                combo.append(num)
                backtrack(num + 1, combo)
                combo.pop()

        combinations = []
        backtrack(1, [])

        return combinations
```

[Permutations](https://leetcode.com/problems/permutations)
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(perm, used) -> None:
            if len(perm) == len(nums):
                permutations.append(perm[:])
                return

            for num in nums:
                if num not in used: 
                    perm.append(num)
                    used.add(num)
                    backtrack(perm, used)
                    perm.pop()
                    used.remove(num)

        permutations = []
        backtrack([], set())
        return permutations

```

[N-Queens II](https://leetcode.com/problems/n-queens-ii)
```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, rows, cols, diags1, diags2) -> None:
            if row == n:
                self.totalQueens += 1
                return

            for col in range(n):
                diag1 = row - col
                diag2 = row + col
                if (
                    row not in rows
                    and col not in cols
                    and diag1 not in diags1
                    and diag2 not in diags2
                ):
                    rows.add(row)
                    cols.add(col)
                    diags1.add(diag1)
                    diags2.add(diag2)
                    backtrack(row + 1, rows, cols, diags1, diags2)
                    rows.remove(row)
                    cols.remove(col)
                    diags1.remove(diag1)
                    diags2.remove(diag2)

        self.totalQueens = 0
        backtrack(0, set(), set(), set(), set())
        return self.totalQueens
```

Key insights to solving this problem:
- labeling the diagonals and keeping them in sets. There are diagonals that go top left to bottom right, and diags that go top right to bottom left; We can identify a diagonal by using arithmetic on the row and col for a placement
- Once we have made a placement, we go to the next row, and we iterate over the columns in the range

[Word Search](https://leetcode.com/problems/word-search)

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(x, y, index) -> bool:
            # If we've matched entire word, return
            if index == len(word):
                return True
            
            # if point is out of bounds or doesn't match next letter, return False
            if x < 0 or x >= len(board) or y < 0 or \
                y >= len(board[0]) or board[x][y] != word[index]:
                return False
            
            # store value at point, set to hashtag to mark as 'seen'
            temp, board[x][y] = board[x][y], '#'

            # visit neighbors
            exists = backtrack(x + 1, y, index + 1) or \
                     backtrack(x, y + 1, index + 1) or \
                     backtrack(x - 1, y, index + 1) or \
                     backtrack(x, y - 1, index + 1)

            # reset the value at board
            board[x][y] = temp

            return exists

        # attempt from every starting position
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
```
