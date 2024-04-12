class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        wi = 0
        ai = 0
        while wi < len(word) and ai < len(abbr):
            if abbr[ai].isdigit():
                if abbr[ai] == "0":
                    return False
                ai_prev = ai
                while ai < len(abbr) and abbr[ai].isdigit():
                    ai += 1
                sub_size = int(abbr[ai_prev:ai])
                if sub_size > len(word) - wi:
                    return False
                wi += sub_size
            else:
                if word[wi] != abbr[ai]:
                    return False
                wi, ai = wi + 1, ai + 1

        return wi == len(word) and ai == len(abbr)
