from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line: List[str] = []
        line_length = 0
        for i in range(len(words) + 1):
            if i == len(words) or line_length + len(line) + len(words[i]) > maxWidth:
                # number of spaces to add between words
                factor = (
                    (maxWidth - line_length) // (len(line) - 1) if len(line) > 1 else 1
                )
                if len(line) == 1:
                    # left justify if just one word
                    line[0] += " " * (maxWidth - line_length)
                else:
                    # fully justify
                    remaining = maxWidth - line_length - (factor * (len(line) - 1))
                    for j in range(remaining):
                        line[j] += " "
                ans.append((" " * factor).join(line))
                line = []
                line_length = 0

            if i < len(words):
                line.append(words[i])
                line_length += len(words[i])
        last_line = ans[-1].split(" ")
        last_line = [s for s in last_line if s != ""]
        last_line_string = " ".join(last_line)
        last_line_string += " " * (maxWidth - len(last_line_string))
        ans[-1] = last_line_string
        print(ans)

        return ans


solution = Solution()
print(
    solution.fullJustify(
        words=["This", "is", "an", "example", "of", "text", "justification."],
        maxWidth=16,
    )
)
print(
    solution.fullJustify(
        words=["What", "must", "be", "acknowledgment", "shall", "be"], maxWidth=16
    )
)
