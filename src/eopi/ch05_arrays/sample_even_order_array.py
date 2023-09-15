""" Given an array, order it such that evens come first """

from typing import List

def evens_first(x: List[int]) -> List[int]:
    l_pointer = 0
    r_pointer = len(x)-1

    while l_pointer < r_pointer:
        if x[l_pointer] % 2:
            if x[r_pointer] % 2:
                r_pointer -= 1
                continue
            else:
                temp = x[l_pointer]
                x[l_pointer] = x[r_pointer]
                x[r_pointer] = temp
        l_pointer += 1

    return x

print(evens_first([1,1,2,2]))
print(evens_first([3,1,2,45,6,1,2,4,56,7,8]))
