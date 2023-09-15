""" Find the First Occurrence of a Substring """

""" 
Give two strings s ('the search text') and t ('the text within which to search'),
find the first occurrence of s in t.
"""

"""
Idea:
    - Sliding window checking for equivalence
Time: O(n^2)
Space: O(1)
"""

def find_first_occurrence(s: str, t: str) -> int:
    pointer = len(s) + 1
    while pointer < len(t):
        # print(t[pointer - (len(s)-1):pointer+1])
        if s == t[pointer - (len(s)-1):pointer+1]:
            return pointer-(len(s)-1)
        pointer += 1
 
print(find_first_occurrence("aabc", "cdaabfaabccdafaabc"))


