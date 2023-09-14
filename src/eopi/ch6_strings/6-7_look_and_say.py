""" Look and Say

E.g. [1,11,21,1211,111221,312211,13112221,1113213211]

Write a program that takes an integer n and returns the nth integer in the look-and-sayseqquence. 
Return the result as a string.
"""

"""
Idea:
    - initialize prev_seq = List[str]; next_seq = List[str]
    - range over input n
    - for each n, loop over sequence with left and right pointers to count digits and ultimately append new values to next
        order in sequencee
    - return the final index in the sequence
"""

from typing import List

def compute_nth_look_and_say(n: int) -> str:
    prev_seq = "1"
    for i in range(n):
        pointer, digit, count, next_seq = 0, prev_seq[0], 0, ""
        while pointer < len(prev_seq):
            # print("pointer %s, count %s, digit %s" % (pointer, count, digit))
            if prev_seq[pointer] != digit:
                next_seq += str(count)
                next_seq += digit
                digit = prev_seq[pointer]
                count = 0
            pointer += 1
            count += 1
        next_seq += str(count)
        next_seq += digit
        prev_seq = next_seq

    return prev_seq

print(compute_nth_look_and_say(0))
print(compute_nth_look_and_say(1))
print(compute_nth_look_and_say(2))
print(compute_nth_look_and_say(3))
print(compute_nth_look_and_say(4))
print(compute_nth_look_and_say(5))
print(compute_nth_look_and_say(6))

import itertools

def compute_nth_look_and_say_pythonic(n: int) -> str:
    s = "1"
    for _ in range (n-1):
        s = ''.join(
                str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s

print("--------------------")
print(compute_nth_look_and_say_pythonic(6))
