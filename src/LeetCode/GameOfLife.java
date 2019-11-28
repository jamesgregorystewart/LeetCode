package LeetCode;


public class GameOfLife {

    public static void main(String[] args) {
        GameOfLife solution = new GameOfLife();
        int[][] board = new int[][] {   {0,1,0},
                                        {0,0,1},
                                        {1,1,1},
                                        {0,0,0}};
        int[][] ans = solution.gameOfLife(board);
        for (int i = 0; i < ans.length; i++) {
            for (int j = 0; j < ans[0].length; j++) {
                System.out.println(ans[i][j]);
            }
        }
    }

    /*
    Input
    * [0,1,0],
      [0,0,1],
      [1,1,1],
      [0,0,0]

      Output
      [0,0,0],
      [1,0,1],
      [0,1,1],
      [0,1,0]

      Rules:
        Any live cell with fewer than two live neighbors dies, as if caused by under-population.
        Any live cell with two or three live neighbors lives on to the next generation.
        Any live cell with more than three live neighbors dies, as if by over-population..
        Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.


      Idea: Encoding
        0 -> 2 is dead to alive
        1 -> -1 is alive to dead

        So:
        - 0 and 2 are dead
        - 1 and -1 are alive
    * */

    private int[][] ans_board;

    private int[][] gameOfLife(int[][] board) {
        this.ans_board = board;

        for (int i = 0; i < ans_board.length; i++) {
            for (int j = 0; j < ans_board[0].length; j++) {
                mutate(new Coordinate(j, i));
            }
        }

        //iterate over the matrix updating the values from their encodings
        for (int i = 0; i < ans_board.length; i++) {
            for (int j = 0; j < ans_board[0].length; j++) {
                if (ans_board[i][j] == -1) ans_board[i][j] = 0;
                else if (ans_board[i][j] == 2) ans_board[i][j] = 1;
            }
        }
        return ans_board;
    }

    //count all the ones and when the required number is met returnf
    private void mutate(Coordinate coord) {
        int sum = 0;
        if (coord.x-1 >= 0 && coord.y-1 >= 0 && Math.abs(ans_board[coord.y-1][coord.x-1]) == 1) sum++;
        if (coord.y-1 >= 0 && Math.abs(ans_board[coord.y-1][coord.x]) == 1) sum++;
        if (coord.x+1 < ans_board[0].length && coord.y-1 >= 0 && Math.abs(ans_board[coord.y-1][coord.x+1]) == 1) sum++;
        if (coord.x+1 < ans_board[0].length && Math.abs(ans_board[coord.y][coord.x+1]) == 1) sum++;
        if (coord.x+1 < ans_board[0].length && coord.y+1 < ans_board.length && Math.abs(ans_board[coord.y+1][coord.x+1]) == 1) sum++;
        if (coord.y+1 < ans_board.length && Math.abs(ans_board[coord.y+1][coord.x]) == 1) sum++;
        if (coord.x-1 >= 0 && coord.y+1 < ans_board.length && Math.abs(ans_board[coord.y+1][coord.x-1]) == 1) sum++;
        if (coord.x-1 >= 0 && Math.abs(ans_board[coord.y][coord.x-1]) == 1) sum++;

        //calculate the new value of the cell
        if (isAlive(coord) && (sum < 2 || sum > 3)) ans_board[coord.y][coord.x] = -1;
        else if (!isAlive(coord) && sum == 3) ans_board[coord.y][coord.x] = 2;
    }

    private boolean isAlive(Coordinate coord) {
        return ans_board[coord.y][coord.x] == 1 || ans_board[coord.y][coord.x] == -1;
    }

    private class Coordinate {
        int x;
        int y;

        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
