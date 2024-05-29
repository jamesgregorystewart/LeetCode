class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0

        num = int(s, 2)
        while num != 1:
            if not num & 1:
                num >>= 1
            else:
                num += 1
            steps += 1
        return steps
