"""Given two arrays, each encoding an integer, return an array representing their product."""

"""
Idea:
    Mimic grade-school multiplication between the two arrays;

Time: O(xy)
Space: O(ab); a = log(x, 10); b = log(y, 10)    log(x)log(y)
"""

from typing import List

def multiply_integers(x: List[int], y: List[int]) -> List[int]:
    res: List[int] = [0] * (len(x) + len(y))

    carry = 0
    for i, i_val in enumerate(reversed(x)):
        res_i = i
        for j, j_val in enumerate(reversed(y)):
            val = (i_val * j_val) + res[res_i] + carry
            res[res_i] = val % 10
            carry = val // 10
            res_i += 1

    if carry != 0:
        res[res_i] = carry
    if res[len(res)-1] == 0:
        # remove leading zero
        del res[len(res)-1]

    # return array back in normal order
    return res[::-1]

print(multiply_integers([1,2,1], [1,3,7]))
print(multiply_integers([9,9], [1]))
print(multiply_integers([9,9], [2]))
print(multiply_integers([2], [2]))
print(multiply_integers([9,9], [9,9]))

