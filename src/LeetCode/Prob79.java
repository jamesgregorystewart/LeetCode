package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class Prob79 {

    public static void main(String[] args) {
        Prob79 solution = new Prob79();

        char[][] board =   {{'A', 'B', 'C', 'E'},
                            {'S', 'F', 'E', 'S'},
                            {'A', 'D', 'E', 'E'}};
        String word = "ABCESEEEF";

        System.out.println(solution.exist(board, word));
    }

    class Coordinate {
        int x;
        int y;
        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    boolean match = false;

    public boolean exist(char[][] board, String word) {
        //find the first letter of the word to begin the backtracking
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    Coordinate coord = new Coordinate(j, i); //j ==> x; i ==> y
                    StringBuilder build = new StringBuilder();
                    boolean[][] visited = new boolean[board.length][board[0].length];
                    build.append(board[i][j]);
                    visited[i][j] = true;

                    backtrack(board, visited, coord, build, word);
                    if (match) return true;
                }
            }
        }
        return false;
    }

    public void backtrack(char[][] board, boolean[][] visited, Coordinate coord, StringBuilder build, String word) {
        if (build.toString().equals(word)) {
            match = true;
        } else if (!match && build.length() < word.length()) {
            List<Coordinate> coords = new ArrayList<>();
            coords.add(new Coordinate(coord.x + 1, coord.y));
            coords.add(new Coordinate(coord.x - 1, coord.y));
            coords.add(new Coordinate(coord.x, coord.y + 1));
            coords.add(new Coordinate(coord.x, coord.y - 1));

            for (Coordinate next : coords) {
                if (next.x >= 0 && next.y >= 0 && next.x < board[0].length && next.y < board.length &&
                        !visited[next.y][next.x] && word.charAt(build.length()) == board[next.y][next.x] && !match) {
                    build.append(board[next.y][next.x]);
                    visited[next.y][next.x] = true;
                    backtrack(board, visited, next, build, word);
                    build.deleteCharAt(build.length() - 1);
                    visited[next.y][next.x] = false;
                }
            }
        }
    }
}
