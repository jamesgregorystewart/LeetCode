""" Compute pow(x,y). Input x is a double, y is an integer. """

def compute_power(x: float, y: int) -> float:
    result, power = 1.0, y
    if y < 0:
        x, power = 1.0 / x, -power

    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1

    return result

print(compute_power(5,3))
print(compute_power(1.181,11))
print(compute_power(7,5))
