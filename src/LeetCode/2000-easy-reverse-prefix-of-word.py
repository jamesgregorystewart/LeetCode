class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse_index = word.find(ch)
        if reverse_index == -1:
            return word

        reverse_segment = word[: reverse_index + 1]
        reverse_segment = reverse_segment[::-1]
        return reverse_segment + word[reverse_index + 1 :]
