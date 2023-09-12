"""
Given an integer encoded as an array, return an array encoding an integer one greater than the input.
"""

"""
Time: O(n)
Space: O(1)
"""



from typing import List

def increment_integer(x: List[int]) -> List[int]:
    for i in reversed(range(len(x))):
        if i == 0 and x[i] + 1 == 10:
            x[i] = 0
            x.insert(0, 1)
            return x
        if x[i] + 1 == 10:
            x[i] = 0
            continue
        x[i] += 1

        return x

print(increment_integer([1,2,3]))
print(increment_integer([1,2,9]))
print(increment_integer([9,9]))
