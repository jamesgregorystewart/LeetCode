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
