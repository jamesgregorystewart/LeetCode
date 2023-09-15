""" Interconvert Strings and Integers

Write a program that will interconvert strings and integers encoding positive or negative integers without using built-in libraries"""

"""
Idea:
    - use array and dict to respectfully perform the conversion digit by digit; handling each case with custom logic

Time: O(n) where n is the length of string, or magnitude of input integer
Space: O(n) Space used is linear with size of input due to string building. 
"""

def interconvert_strings_and_integers(x: int | str) -> int | str:
    int_to_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    str_to_int = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

    def convert_str_to_int(x: str) -> int:
        sign = 1
        start = 0
        if x[0] == '-':
            sign = -1
            start = 1
        y = 0
        for i in range(start, len(x)):
            y = (y * 10) + str_to_int[x[i]]
        return y*sign

    def convert_int_to_str(x: int) -> str:
        y = ""
        negative = False
        if x < 0:
            negative = True
            x *= -1
        while x > 0:
            y += int_to_str[x % 10]
            x //= 10
        if negative:
            y += "-"
        return y[::-1]


    if type(x) == int:
        return convert_int_to_str(x)
    return convert_str_to_int(x)

print(type(interconvert_strings_and_integers("123")))
print(type(interconvert_strings_and_integers(123)))
print(interconvert_strings_and_integers("-123"))
print(interconvert_strings_and_integers(-123))


# Super impressive one-liner for string to int
def string_to_int(s: str) -> int:
    return (-1 if s[0] == '-' else 1) * functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), s[s[0] in '-+':], 0)
