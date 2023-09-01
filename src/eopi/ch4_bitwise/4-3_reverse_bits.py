"""
Write a program that takes as input a 64-bit unsigned int 
    and returns the input as a 64-bit integer consisting of the bits of the input in reverse order.
"""

"""
Idea: Brute Force; iterate through bits toggling them if different
"""
def reverse_bits(x: int) -> int:
    bit_length = x.bit_length()

    for i in range(bit_length//2):
        if (x >> i) & 1 != (x >> (bit_length-(i+1)) & 1):
            bit_mask = (1 << i) | (1 << (bit_length-(i+1)))
            x ^= bit_mask
    return x


# 1234: 10011010010
print(bin(reverse_bits(1234))
