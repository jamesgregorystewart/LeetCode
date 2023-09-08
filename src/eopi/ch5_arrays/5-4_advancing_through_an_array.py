""" Given an array where each element denotes the maximum numbe of moves you may move forward from its index,
write a program which will determine whether it is possible to reach the end. """

"""
Time: O
"""


from typing import List

def advance_array(x: List[int]) -> bool:
    stack = []
    pointer = 0
    while True:
        if pointer + x[pointer] >= len(x):
            return True
        if x[pointer] != 0:
            if x[pointer] > 1:
                stack.append((pointer, x[pointer]))
            pointer += x[pointer]
        else:
            if len(stack) == 0:
                return False

            pointer, jump = stack.pop()
            jump -= 1
            if jump > 1:
                stack.append((pointer, jump))
            pointer += jump

print(advance_array([3,3,1,0,2,0,1]))
print(advance_array([3,2,0,0,2,0,1]))
print(advance_array([0,1]))

def can_reach_end(x: List[int]) -> bool:
    furthest_reach_so_far, last_index = 0, len(x) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, x[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index


print(can_reach_end([0,0,0,0,0,7]))
