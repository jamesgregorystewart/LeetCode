import functools
import string

a = "-1234"
"""
functools.reduce -> takes a function (lambda), iterator, and an initial value
lambda -> takes two args and performs some operation iteratively with them
"""
stringified = (-1 if a[0] == '-' else 1) * functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c), a[a[0] in '-+':], 0)
print(stringified)


