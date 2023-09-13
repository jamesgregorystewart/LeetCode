""" Palindromatic String

Write a program that tests if a string is palindromatic less any non alpha characters"""

"""
Time: O(n)
Space: O(1)
"""

import string

def is_string_palindromatic(s: str) -> bool:
    l, r = 0, len(s)-1
    
    while l < r:
        if s[l] not in string.ascii_letters:
            l += 1
            continue
        if s[r] not in string.ascii_letters:
            r -= 1
            continue

        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False

    return True

print(is_string_palindromatic("A man, a plan, a canal, Panama"))
print(is_string_palindromatic("      y"))
print(is_string_palindromatic("Ray a Ray"))
