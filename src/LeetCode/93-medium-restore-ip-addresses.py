from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def isValid(term) -> bool:
            return len(term) == 1 or (
                term[0] != "0" and (1 <= len(term) <= 3) and 1 <= int(term) <= 255
            )

        N = len(s)
        for i in range(1, min(4, N - 2)):
            if not isValid(s[:i]):
                continue
            for j in range(i + 1, min(i + 4, N - 1)):
                if not isValid(s[i:j]):
                    continue
                for k in range(j + 1, min(j + 4, N)):
                    if not isValid(s[j:k]) or not isValid(s[k:]):
                        continue
                    result.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
        return result
