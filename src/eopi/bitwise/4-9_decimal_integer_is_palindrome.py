""" Check if a decimal integer is a palindrome """

"""
Optimization would be to compare right and left side digits till center; saves on space and time
"""

def is_int_palindrome(x: int) -> bool:
    if x < 0:
        return False

    pal = 0
    x_ref = x
    while x_ref > 0:
        pal = (pal * 10) + (x_ref % 10)
        x_ref //= 10

    return (pal == x)


print(is_int_palindrome(0))
print(is_int_palindrome(123))
print(is_int_palindrome(2332))

from math import floor, log

def is_int_palindrome_optimized(x: int) -> bool:
    if x < 0:
        return False
    
    while x >= 10:
        length = floor(log(x, 10))+1

        MSD = x // (10**(length-1))
        LSD = x % 10


        print("x: %s, length: %s, MSD: %s, LSD: %s" % (x, length, MSD, LSD))

        if LSD != MSD:
            return False
        
        x %= (10**(length-1))
        x //= 10

    return True


print(is_int_palindrome_optimized(1))
print(is_int_palindrome_optimized(121))
print(is_int_palindrome_optimized(12))

# print(floor(log(1234, 10))+1)

# print(1234//(10**((floor(log(1234, 10))+1)-1)))

# get length of int via math.floor(math.log(x, 10))+1

# get last MSD of int via x // 10**(length-1)
