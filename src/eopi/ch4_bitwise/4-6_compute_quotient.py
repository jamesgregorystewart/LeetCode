"""Compute quotient of two integers using bitwise operations, shifts, addition, and subtraction"""

def compute_quotient(x: int, y: int) -> int:
    if x == 0:
        return 0

    quotient = 0

    k = x.bit_length() - y.bit_length()
    while x >= y:
        if y << k <= x: # replace mult with bitwise operations
            quotient += (1<<k)
            x -= y << k # replace mult with bitwise operations
        k -= 1

    return quotient


print(compute_quotient(128, 11))
print(compute_quotient(132, 11))
