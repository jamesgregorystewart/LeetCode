class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag1 = 0
        self.diag2 = 0

    def move(self, row: int, col: int, player: int) -> int:
        x = 1 if player == 1 else -1
        self.row[row] += x
        self.col[col] += x
        if row == col:
            self.diag1 += x
        d2c = self.n - col - 1
        if row == d2c:
            self.diag2 += x
        if (
            abs(self.row[row]) == self.n
            or abs(self.col[col]) == self.n
            or abs(self.diag1) == self.n
            or abs(self.diag2) == self.n
        ):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
