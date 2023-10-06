""" Evaluate RPN Expressions """

"""
Given an RPN expression as a string, e.g. "1,2,+,-2,x" return its evaluated output as an integer
"""

"""
Idea use a stack, and when an operator is encountered, pop all elements, perform operation, and push back onto stack.
Return final operand in stack as output.

TRICKS:
    - put operators into a set with lambda functions as values
    - split input on the delimiter (duh)
"""

import string
from typing import List

def evaluateRPN(s: str) -> int:
    if not s:
        return -1

    stack = []
    i = 0
    while i < len(s):
        c = s[i]
        if c in string.digits or (c == '-' and i < len(s)-1 and s[i+1] in string.digits):
            # build the integer
            sign = -1 if c == '-' else 1
            num = 0
            start = i if sign == 1 else i + 1
            for j in range(start,len(s)):
                if s[j] not in string.digits:
                    break
                num = num * 10 + int(s[j])
            i = j - 1
            stack.append(num * sign)
        elif c not in string.digits and c != ",":
            op2, op1 = int(stack.pop()), int(stack.pop())
            res = 0
            match c:
                case '+':
                    stack.append(op1 + op2)
                case '-':
                    stack.append(op1 - op2)
                case 'x':
                    stack.append(op1 * op2)
                case '/':
                    stack.append(op1 // op2)
        i += 1
    
    return int(stack.pop())

# print(evaluateRPN("1,2,+,-2,x"))
# print(evaluateRPN("1729"))
# print(evaluateRPN("3,4,+,2,x,1,+"))
# print(evaluateRPN("1,1,+,-2,x"))
# print(evaluateRPN("-641,6,/,28,/"))


def cleanRPNEvaluation(s: str) -> int:
    intermediate_results: List[int] = []
    delimiter = ','
    operators = { # can put lambda functions as value -- mindblown
            '+': lambda y, x : x + y, '-': lambda y, x: x - y,
            'x': lambda y, x : x * y, '/': lambda y, x: x // y
    }

    for token in s.split(delimiter):
        if token in operators: # don't need to say operators.keys(), will default to this
            intermediate_results.append(operators[token](intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
    return intermediate_results[-1]

print(cleanRPNEvaluation("1,2,+,-2,x"))
print(cleanRPNEvaluation("1729"))
print(cleanRPNEvaluation("3,4,+,2,x,1,+"))
