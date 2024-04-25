from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []

        for log in logs:
            parts = log.split()
            if parts[1].isdigit():
                digit_logs.append(parts)
            else:
                letter_logs.append(parts)
        letter_logs.sort(key=lambda x: (x[1:], x[0]))
        return [" ".join(log) for log in letter_logs] + [
            " ".join(log) for log in digit_logs
        ]
