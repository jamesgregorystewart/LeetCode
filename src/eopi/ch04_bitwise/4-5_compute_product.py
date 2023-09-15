"""
Compute product of integers x and y without arithmetic operations.
"""


def bitwise_product_solution(x: int, y: int) -> int:
    def add(a, b):
        # a ^ b performs add w/o carry
        # a & b << 1 identifies carry location, and moves it
        return a if b == 0 else add(a ^ b, (a & b) << 1)

    running_sum = 0
    while x:
        if x & 1: # check if bit set to 1
            running_sum = add(running_sum, y) # sum y to running sum
        x, y = x >> 1, y << 1 # x used as indicator for when to sum; y is summed
    return running_sum

print(bitwise_product_solution(3, 5))
print(bitwise_product_solution(4, 5))
