from time import sleep

def divide_with_bitshifts(dividend: int, divisor: int):

    quotient = 0

    while dividend >= divisor:
        current_divisor = divisor
        multiple = 1

        while dividend >= (current_divisor << 1):
            current_divisor <<= 1 
            multiple <<= 1

        dividend -= current_divisor
        quotient += multiple

    return quotient


print(divide_with_bitshifts(dividend=10, divisor=3))

