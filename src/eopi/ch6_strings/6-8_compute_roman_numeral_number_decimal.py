""" Convert From Roman to Decimal

LIX -> 59
XXXXXIIIIIIIII -> 59
LVIIII -> 59

Symbols must appear in decreasing order except in the case where:
    - I can immediately precede V and X
    - X can immediately precede L and C
    - C can immediately precede D and M

Back to back exceptions are not allowed, e.g., IXC is invalid, as is CDM
"""

"""
Idea:
    - sum values of symbols left to right if they are nonincreasing
    - where an increase is found, check exception rules, perform valid subtractions, or return invalid
    - actually makes more sense to go from right to left

Time: O(n)
Space: O(1)
"""



from typing import List

def convert_roman_to_decimal(roman: str) -> int:
    conversion_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    pointer, decimal = len(roman)-1, 0
    increasing = False
    while pointer >= 0:
        symbol = roman[pointer]
        if pointer < len(roman) - 1 and conversion_map[symbol] < conversion_map[roman[pointer+1]]:
            if roman[pointer+1] in 'VX' and symbol == 'I' or roman[pointer+1] in 'LC' and symbol == 'X' or roman[pointer+1] in 'DM' and symbol == 'C':
                if increasing:
                    return -1
                increasing = True
                # do a subtraction loop
                prev_symbol = symbol
                while symbol == prev_symbol and pointer >= 0:
                    decimal -= conversion_map[prev_symbol]
                    pointer -= 1
                    prev_symbol, symbol = symbol, roman[pointer]
            else:
                # nonincreasing symbols found which aren't within the exception case
                return -1
        else:
            decimal += conversion_map[symbol]
            pointer -= 1
            increasing = False
    return decimal

print(convert_roman_to_decimal("LVIIII"))
print(convert_roman_to_decimal("LIX"))
print(convert_roman_to_decimal("XXXXXIIIIIIIII"))
print(convert_roman_to_decimal("IXC"))


"""
This is how you do it if you are an expert in python
"""

import functools

def convert_roman_to_decimal_pythonic(roman: str) -> int:
    T = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
            lambda val, i: val + (-T[roman[i]] if T[roman[i]] < T[roman[i+1]] else T[roman[i]]), reversed(range(len(roman)-1)), T[roman[-1]])

print(convert_roman_to_decimal_pythonic("LVIIII"))
