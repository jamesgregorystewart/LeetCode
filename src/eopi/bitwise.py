"""Complete the following in O(1) time"""
# Right propagate the right-most set bit e.g. 01010000 -> 01011111
def right_propagate(x: int) -> int:
    return (x | (x-1))

print("Problem: Right Propagate %s" % bin(right_propagate(40)))
print("\n-------------------\n")


# Compute x mod a power of two e.g. 13 for 77 mod 64
def bitwise_modulo(dividend: int, divisor: int) -> int:
    print("Problem: Bitwise Modulo")
    # 77: 1001101
    # 64: 1000000
    # 13: 0001101
    print("dividend: %s" % bin(dividend))
    print("divisor: %s" % bin(divisor))

    print("If we just did a XOR we would get: %s" % (dividend ^ divisor))

    # FIRST: XOR dividend and divisor
    res = dividend ^ divisor
    print("res: %s" % bin(res))

    # SECOND: mask bits greater than MSB of divisor
    # 1) create two masks, and XOR them
    dividend_mask = 1 << dividend.bit_length()
    dividend_mask |= dividend_mask - 1
    print("dividend mask: %s %s" % (bin(dividend_mask), dividend_mask.bit_length()))

    divisor_mask = 1 << divisor.bit_length()
    divisor_mask |= divisor_mask - 1
    print("divisor mask: %s %s" % (bin(divisor_mask), divisor_mask.bit_length()))

    mask = dividend_mask ^ divisor_mask
    print("mask: %s" % bin(mask))

    # Finally: apply mask
    # to apply mask we must first make sure all bits above are set,
    # then we toggle them with XOR 
    res = (res | mask)
    print("res1 %s" % bin(res))
    res ^= mask
    print("res: %s" % bin(res))

    return res

print(bitwise_modulo(77, 64))
print("\n-------------------\n")

# Test if x is a power of 2 e.g. x=1,2,4,8,... is True, else False
def is_power_of_two(x: int) -> bool:
    # if x is a power of 2 it should have 1 bit set
    # so & x with 1 minus itself and it should be 0
    return x > 0 and (x & (x -1)) == 0

print(is_power_of_two(2))
print(is_power_of_two(3))
print(is_power_of_two(64))
print(is_power_of_two(77))
