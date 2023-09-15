""" Reverse the digits of an integer. E.g. 123 -> 321 or -413 -> -314 """

def reverse_digits(x: int) -> int:
    negative = True if x < 0 else False
    x = abs(x)
    res = 0
    while x > 0:
        res = (res * 10) + (x % 10)
        x //= 10
    return res * -1 if negative else res
    

print(reverse_digits(123))
print(reverse_digits(-1234))
