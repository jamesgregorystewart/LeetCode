class Solution:
    def findLatestTime(self, s: str) -> str:
        parts = s.split(":")

        if parts[0][0] == "?":
            if parts[0][1] not in ["0", "1", "?"]:
                parts[0] = "0" + parts[0][1]
            else:
                parts[0] = "1" + parts[0][1]
        if parts[0][1] == "?":
            if parts[0][0] == "0":
                parts[0] = parts[0][0] + "9"
            else:
                parts[0] = parts[0][0] + "1"

        if parts[1][0] == "?":
            parts[1] = "5" + parts[1][1]
        if parts[1][1] == "?":
            parts[1] = parts[1][0] + "9"

        return ":".join(parts)
