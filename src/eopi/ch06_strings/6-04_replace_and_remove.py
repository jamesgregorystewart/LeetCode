""" Replace and Remove

Given an input string, and an integer representing the number of characters on which to operate
return an array of characters/string wherein all 'a's are replaced with 'dd' and all 'b's are
removed"""

"""
Idea:
    - Two-pass technique; first left to right pass will remove all 'b' instances with rewrite
    - Second pass is right to left replacing all 'a' instances with 'dd'

"""

def replace_and_remove(chars: str, k: int) -> str:

