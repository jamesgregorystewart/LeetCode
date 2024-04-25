class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_parts, v2_parts = version1.split("."), version2.split(".")

        v1_i, v2_i = 0, 0
        while v1_i < len(v1_parts) and v2_i < len(v2_parts):
            if int(v1_parts[v1_i]) < int(v2_parts[v2_i]):
                return -1
            if int(v1_parts[v1_i]) > int(v2_parts[v2_i]):
                return 1
            v1_i, v2_i = v1_i + 1, v2_i + 1
        while v1_i < len(v1_parts):
            if int(v1_parts[v1_i]) > 0:
                return 1
            v1_i += 1
        while v2_i < len(v2_parts):
            if int(v2_parts[v2_i]):
                return -1
            v2_i += 1

        return 0
