""" PROBLEM 

Given a random number generator which outputs 0 | 1, write a program which outputs a random 
integer between input integers a and b (inclusive) with equal probability.

"""

""" IDEA

find how many bits it would take to represent the upper bound of int to generate; then iterate
through the bit indices and flip each per gen_rand(); regenerate if number is outside range

Notes:
    - Used ceil(log(b), 2) to find the number of bits required, and thus loop iterations


Time complexity: O(log(b-a+1))
Space complexity: O(1)

time complexity is such because of the independent nature of the rolls, and the convergent
chart of tries exceeding the max bound, while res > b can be described with O(1); it is thus
the number of bits required to represent the word which determines the time complexity -- 
O(log(b-a+1))

"""


from random import randrange

def gen_rand() -> int:
    return randrange(0,2) # start inclusive; end exclusive


from math import ceil, log, inf

def random_number_generator(a: int, b: int) -> int:
    res = inf 
    while res > b:
        print("res: %s; b: %s" % (res, b))
        res = 0
        for i in range(ceil(log((b-a+1), 2))):
            res ^= (gen_rand() << i)
        res += a

    return res

num = random_number_generator(0, 121)
print("%s   %s" % (bin(num), num))
