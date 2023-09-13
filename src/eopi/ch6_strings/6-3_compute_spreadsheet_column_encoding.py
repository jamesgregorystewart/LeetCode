""" Compute Spreadsheet Column Encoding

Given a spreadsheet column, return its ordinal position in decimal"""

"""
Idea:
    - Use the unicode encodings of A-Z to find the decimal value of base-26 alphabet
    - Use functools.reduce and lambda function to map the column to its value

Time: O(n)
Space: O(1)
"""

import functools

def compute_spreadsheet_col(col: str) -> int:
    return functools.reduce(
            lambda x, c: x * 26 + (ord(c) - ord('A') + 1), col, 0
    )

print(compute_spreadsheet_col("A"))
print(compute_spreadsheet_col("ZZ"))
