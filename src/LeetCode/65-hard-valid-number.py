class Solution:
    def isNumber(self, s: str) -> bool:
        decimal = False
        e = False
        digit = False
        for i, c in enumerate(s):
            if c.isdigit():
                digit = True
            elif c in ["-", "+"]:
                if i > 0 and s[i - 1] not in ["e", "E"]:
                    return False
            elif c in ["e", "E"]:
                if e or not digit:
                    return False
                e = True
                digit = False
            elif c == ".":
                if decimal or e:
                    return False
                decimal = True
            else:
                # we don't know what you are
                return False
        return digit
