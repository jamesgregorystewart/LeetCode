"""Implement code that takes as input a 64-bit integer and swaps the bits at indicies i and j."""

"""
Idea: extract both, and set the opposite accordingly
"""

def swap_bits(x: int, i: int, j: int) -> int:

    res = x

    i_mask = 1 << i
    print("i_mask: %s" % bin(i_mask))
    j_mask = 1 << j
    print("j_mask: %s" % bin(j_mask))
    print("ith bit: %s" % (x & i_mask))
    print("jth bit: %s" % (x & j_mask))

    i_bit = x & i_mask
    j_bit = x & j_mask

    res = flip_bit(i_bit, j, res)
    res = flip_bit(j_bit, i, res)

    return res

def flip_bit(bit: int, loc: int, res: int) -> int:
    if bit > 0:
        res |= (1 << loc)
    else:
        res &= ~(1 << loc)

    return res

print(bin(swap_bits(13, 0, 1)))


"""
Idea: if the bits are the same, do nothing, if they differ, just flip them 
O(1) / O(1)
"""
def swap_bits_optimized(x: int, i: int, j: int) -> int:
    if (x >> i) & 1 != (x >> j) & 1:
        x ^= 1 << i
        x ^= 1 << j
    return x


print(bin(swap_bits_optimized(13, 0, 1)))
