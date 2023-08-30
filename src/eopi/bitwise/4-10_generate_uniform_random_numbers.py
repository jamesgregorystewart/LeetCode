""" 

Given a random number generator which outputs 0 | 1, write a program which outputs a random 
integer between input integers a and b (inclusive) with equal probability.

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
        for i in range(ceil(log((b-1), 2))):
            res ^= (gen_rand() << i)
        res += a

    return res

num = random_number_generator(0, 121)
print("%s   %s" % (bin(num), num))
