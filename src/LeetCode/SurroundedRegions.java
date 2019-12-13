package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class SurroundedRegions {

    public static void main(String[] args) {
        SurroundedRegions solution = new SurroundedRegions();
        char[][] board = new char[][] { {'X','O','X','X'},
                                        {'X', 'O', 'O', 'X'},
                                        {'X','X','O','X'},
                                        {'X','O','X','X'}};
        solution.solve(board);

        for (char[] row : board) for (char c : row) System.out.println(c);
    }

    /*
    * Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    Example:

    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X
    Explanation:

    Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

    Idea:
    - Pre-process - Iterate around border and BFS from every 'O' flipping to a 'Z' that we will flip back to 'O' in post-processing step
    - Process - Iterate through the grid starting at [1,1] flipping all 'O's with 'X'
    - Post-process - Iterate through grid swtiching all Z's back to O's

    Possible improvements: store all Z's so that we can more quickly change them back to Os (faster but more memory)
    * */

    public void solve(char[][] board) {
        if (board.length == 0) return;
        if (board[0].length == 0) return;
        int cols = board[0].length;
        int rows = board.length;

        //Pre-Process
        //top and bottom rows
        for (int i = 0; i < cols; i++) {
            if (board[0][i] == 'O') bfs(board, new Coordinate(i, 0));
            if (board[rows-1][i] == 'O') bfs(board, new Coordinate(i, rows-1));
        }
        //left and right columns
        for (int i = 0; i < board.length; i++) {
            if (board[i][0] == 'O') bfs(board, new Coordinate(0, i));
            if (board[i][cols-1] == 'O') bfs(board, new Coordinate(0, cols-1));
        }

        //Process + Post-process steps
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                board[i][j] = board[i][j] == 'O' ? 'X' : board[i][j];
                board[i][j] = board[i][j] == 'Z' ? 'O' : board[i][j];
            }
        }
    }

    private void bfs(char[][] board, Coordinate coord) {
        board[coord.y][coord.x] = 'Z';
        List<Coordinate> coords = new ArrayList<>();
        coords.add(new Coordinate(coord.x-1, coord.y));
        coords.add(new Coordinate(coord.x+1, coord.y));
        coords.add(new Coordinate(coord.x, coord.y-1));
        coords.add(new Coordinate(coord.x, coord.y+1));
        for (Coordinate next : coords) {
            if (next.x >= 0 && next.x < board[0].length && next.y >= 0 && next.y < board.length && board[next.y][next.x] == 'O') {
                bfs(board, next);
            }
        }
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
