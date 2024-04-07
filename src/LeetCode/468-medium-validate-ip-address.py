from typing import List


class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        def is_ip4(parts: List[str]) -> str:
            for part in parts:
                if not part or len(part) > 1 and part[0] not in ["1", "2"]:
                    return "Neither"
                try:
                    num = int(part)
                    if 0 > num or num > 255:
                        return "Neither"
                except ValueError:
                    return "Neither"
            return "IPv4"

        def is_ip6(parts: List[str]) -> str:
            for part in parts:
                if not part or len(part) > 4:
                    return "Neither"
                try:
                    hex = int(part, 16)
                    if hex < 0 or hex > int("ffff", 16):
                        return "Neither"
                except ValueError:
                    return "Neither"

            return "IPv6"

        ip4_parts = queryIP.split(".")
        ip6_parts = queryIP.split(":")
        if len(ip4_parts) == 4:
            return is_ip4(ip4_parts)
        if len(ip6_parts) == 8:
            return is_ip6(ip6_parts)

        return "Neither"
