class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, rows, cols, diags1, diags2) -> None:
            if row == n:
                self.totalQueens += 1
                return

            for col in range(n):
                diag1 = row - col
                diag2 = row + col
                if (
                    row not in rows
                    and col not in cols
                    and diag1 not in diags1
                    and diag2 not in diags2
                ):
                    rows.add(row)
                    cols.add(col)
                    diags1.add(diag1)
                    diags2.add(diag2)
                    backtrack(row + 1, rows, cols, diags1, diags2)
                    rows.remove(row)
                    cols.remove(col)
                    diags1.remove(diag1)
                    diags2.remove(diag2)

        self.totalQueens = 0
        backtrack(0, set(), set(), set(), set())
        return self.totalQueens
