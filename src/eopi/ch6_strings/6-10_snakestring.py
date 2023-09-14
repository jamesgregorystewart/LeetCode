""" Snakestring """

""" Refer to EOPI 6.10 on page 80 for explanation on snakestring"""

"""
Idea:
    - find periodicity for when a character is on top, middle, and bottom
    - iterate 3 pointers simultaneously building three strings
    - join together at end

Time: O(n)
Space: O(n)
"""


def compute_snakestring(s: str) -> str:
    top, mid, bot = 1, 0, 3
    parts = [""] * 3
    while True:
        if top >= len(s) and mid >= len(s) and bot >= len(s):
            return ''.join(parts)
        if top < len(s):
            parts[0] += s[top]
            top += 4
        if mid < len(s):
            parts[1] += s[mid]
            mid += 2
        if bot < len(s):
            parts[2] += s[bot]
            bot += 4

print(compute_snakestring("Hello World!"))


"""
The pythonic way to do it, duh!
"""

def compute_snakestring_pythonic(s: str) -> str:
    return (s[1::4] + s[0::2] + s[3::4])

print(compute_snakestring_pythonic("Hello World!"))
