""" Run-Length Encoding """

""" 
aaaabcaa -> 4abc2a

Time: O(n)
Space: O(n)
"""

import functools
import itertools
import string

class Encoder:

    def encode(self, s: str) -> str:
        pointer, counter = 0, 1
        res = ""
        while pointer < len(s)-1:
            if s[pointer+1] != s[pointer]:
                res += (str(counter) if counter > 1 else "") + s[pointer]
                counter = 0
            pointer += 1
            counter += 1
        res += (str(counter) if counter > 1 else "") + s[pointer]
        return res

    def decode(self, s: str) -> str:
        pointer, res = 0, ""
        while pointer < len(s):
            if s[pointer] in string.digits:
                res += s[pointer+1] * (int(s[pointer]))
                pointer += 2
            else:
                res += s[pointer]
                pointer += 1
        return res


encoder = Encoder()
print(encoder.encode("aaaabcaa"))
print(encoder.decode(encoder.encode("aaaabcaa")))
