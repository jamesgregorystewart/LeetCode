class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or (not s[0].isdigit() and s[0] not in ["-", "+"]):
            return 0

        positive = True if s[0].isdigit() or s[0] == "+" else False

        left = 0 if s[0].isdigit() else 1
        if left == len(s) or not s[left].isdigit():
            return 0
        for right in range(left, len(s)):
            if not s[right].isdigit() or right == len(s) - 1:
                modifier = 0 if not s[right].isdigit() else 1
                if positive:
                    return min(2**31 - 1, int(s[left : right + modifier]))
                else:
                    return max((2**31) * -1, int(s[left : right + modifier]) * -1)
        return 0
