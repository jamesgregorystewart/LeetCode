""" Compute All Valid IP Addresses

19216811 -> 9 possibilities, e.g., 192.6.81.1
"""

"""
Idea:
    - use nested for loops to test periods in all possible locations without overlap
    - limit possibilities with constraint on format of each part, e.g., part <= 255

Time: O(1) because there are 2^32 possibilities
"""

from typing import List

def get_valid_ip_addresses(s: str) -> List[str]:
    def is_valid_part(s):
        # '00', '000', '01' are not valid, '0' is valid
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)

    result, parts = [], [''] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i + j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
    return result

print(get_valid_ip_addresses("19216811"))
