package LeetCode;

public class TicTacToe {

    /*
    * maintain array for rows
    * maintain array for cols
    * if any cell in either reaches n, return that player's success
    *
    * maintain variable for diagonal
    * maintain variable for antidiagonal
    * if either of these diagonals reaches n, return that player's success
    * */

    int[] p1_rows;
    int[] p1_cols;
    int p1_diagonal;
    int p1_anti_diagonal;

    int[] p2_rows;
    int[] p2_cols;
    int p2_diagonal;
    int p2_anti_diagonal;

    int n;

    /** Initialize your data structure here. */
    public TicTacToe(int n) {
        p1_rows = new int[n];
        p1_cols = new int[n];
        p1_diagonal = 0;
        p1_anti_diagonal = 0;

        p2_rows = new int[n];
        p2_cols = new int[n];
        p2_diagonal = 0;
        p2_anti_diagonal = 0;

        this.n = n;
    }

    /** Player {player} makes a move at ({row}, {col}).
     @param row The row of the board.
     @param col The column of the board.
     @param player The player, can be either 1 or 2.
     @return The current winning condition, can be either:
     0: No one wins.
     1: Player 1 wins.
     2: Player 2 wins. */
    public int move(int row, int col, int player) {
        if (player == 1) {
            p1_rows[row]++;
            if (p1_rows[row] == n) return 1;
            p1_cols[col]++;
            if (p1_cols[col] == n) return 1;
            if (row == col) p1_diagonal++;
            if (row + col == n-1) p1_anti_diagonal++;
            if (p1_diagonal == n || p1_anti_diagonal == n) return 1;
        } else {
            p2_rows[row]++;
            if (p2_rows[row] == n) return 2;
            p2_cols[col]++;
            if (p2_cols[col] == n) return 2;
            if (row == col) p2_diagonal++;
            if (row + col == n-1) p2_anti_diagonal++;
            if (p2_diagonal == n || p2_anti_diagonal == n) return 2;
        }
        return 0;
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */
