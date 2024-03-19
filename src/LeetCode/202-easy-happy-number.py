class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n:
            if n in seen:
                return False
            if n == 1:
                return True
            seen.add(n)
            t = n
            sum = 0
            while t:
                sum += (t % 10) ** 2
                t //= 10
            n = sum
        return False
