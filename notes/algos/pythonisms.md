# Pythonisms

## Lambdas 

Problem: [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=daily-question&envId=2024-01-30)
Example using lambdas as values in a matrix to help calculate reverse polish notation
```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = {
                '+': lambda y, x: x + y, '-': lambda y, x: x - y,
                '*': lambda y, x: x * y, '/': lambda y, x: ceil(x / y) if (x < 0) ^ (y < 0) else floor (x / y)
                }
        for token in tokens:
            if token in operators:
                operands.append(operators[token](operands.pop(), operands.pop()))
            else: 
                operands.append(int(token))

        return operands.pop()

```

## Testing Framework

### General Testing of classes with methods that return a value

It will be smart to use a testing framework when in interviews for clarity. Here's how I can use unittest module in python:

```python
from typing import List, Tuple
import collections
import unittest
import copy


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def sink(queue) -> None:
            self.islands += 1
            moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            while queue:
                coord = queue.popleft()
                for move in moves:
                    x, y = coord[0] + move[0], coord[1] + move[1]
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                        grid[x][y] = "0"  # key is to set to 0 as you find the neighbors
                        queue.append((x, y))

        self.islands = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    sink(collections.deque([(i, j)]))
        return self.islands


class TestSolution(unittest.TestCase):
    def setUp(self):
        # This will run before each test, setting each up
        self.solution = Solution()
        self.grid = [["0"] * 5 for _ in range(5)]
        grid = [["0"] * 5 for _ in range(5)]

    def test_empty_grid(self):
        self.assertEqual(self.solution.numIslands([]), 0)

    def test_no_islands(self):
        grid = [["0"] * 3 for _ in range(3)]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_no_land(self):
        # grid = [["1"] * 3 for _ in range(3)]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_one_island(self):
        grid = [["0"] * 3 for _ in range(3)]
        grid[1][1] = "1"
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_multiple_disconnected_islands(self):
        t_grid = copy.deepcopy(self.grid)
        t_grid[0][1] = "1"
        t_grid[1][1] = "1"
        t_grid[2][2] = "1"
        self.assertEqual(self.solution.numIslands(t_grid), 2)


if __name__ == "__main__":
    unittest.main() # this will run all the tests
```

Additional notes are that I used the conditional `if __name__ == '__main__'` which means that this script cannot be imported, it can only be executed as a script standalone.


### Testing Functions with No Return value

1. Verify Side Effects
2. Mock External Systems
3. Assert on Called Functions

```python
def add_item_to_list(item, target_list=[]):
    target_list.append(item)
    # No return value

import unittest
from unittest.mock import MagicMock

class TestAddItemToList(unittest.TestCase):
    def test_add_item_to_list(self):
        test_list = []
        add_item_to_list('test_item', test_list)
        self.assertIn('test_item', test_list)  # Verify the side effect
```

### Testing a function that calls another function

1. Test the outer function's behavior OR
2. Refactor to increase testability

```python
# For a function that calls another function, mock the called function:
def process_data(data):
    # Imagine this calls another function that we want to mock
    result = external_function(data)
    # Do something with the result (not shown here)

class TestProcessData(unittest.TestCase):
    def test_process_data_calls_external_function(self):
        with unittest.mock.patch('__main__.external_function') as mock_func:
            mock_func.return_value = 'mocked result'
            process_data('data')
            mock_func.assert_called_once_with('data')  # Assert it was called correctly
```
