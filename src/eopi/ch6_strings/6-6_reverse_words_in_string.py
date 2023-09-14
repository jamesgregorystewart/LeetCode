""" Reverse all the words in a sentence """

""" Bob likes Alice -> Alice likes Bob """

"""
Idea:
    - split s on space, two for loops to write chars from words[] in reverse order to 
    a new string to be return, or the same string
"""

"""
Time: O(n) First reverse of string is O(n); Iterating through array reversing each word is another O(n)
Space: O(1) Constant memory; modify input array
"""

from typing import List

def reverse_words_in_sentence(s: List[str]) -> [str]:
    def reverse_substring(s: str, start: int, end: int) -> None:
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1

    reverse_substring(s, 0, len(s)-1)

    l, r = 0, 0
    while True:
        if s[r] == ' ':
            reverse_substring(s, l, r - 1)
            l, r = r + 1, r + 2
        elif r == len(s) -1:
            reverse_substring(s, l, r)
            return s
        else:
            r += 1

print(reverse_words_in_sentence(list("Alice likes Bob")))
