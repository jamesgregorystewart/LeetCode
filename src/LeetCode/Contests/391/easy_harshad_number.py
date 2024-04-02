class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        d = x
        sum = 0
        while d:
            sum += d % 10
            d //= 10
        return -1 if x % sum else sum
