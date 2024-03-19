class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = ""
        step = (numRows - 1) * 2
        for i in range(numRows):
            # i is our starting index for each row
            for j in range(i, len(s), step):
                ans += s[j]
                if i > 0 and i < numRows - 1:
                    mid_step = step - (i * 2)
                    if j + mid_step < len(s):
                        ans += s[j + mid_step]
        return ans
