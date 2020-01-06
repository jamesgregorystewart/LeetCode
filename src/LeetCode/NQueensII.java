package LeetCode;

import java.util.*;

public class NQueensII {

    public static void main(String[] args) {

    }

    /*
    * The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



    Given an integer n, return the number of distinct solutions to the n-queens puzzle.

    Example:

    Input: 4
    Output: 2
    Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    * */

    /*
    * Idea: backtracking using sets to show available columns/rows
    * */

    //TODO: continue this another time

    public int totalNQueens(int n) {
        if (n <= 1) return 0;
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();
        for (int i = 0; i < n; i++) {
            rows.add(i);
            cols.add(i);
        }
        int result = 0;





        return result;
    }

    class Board {
        List<Coordinate> queenPositions;

        public Board(int size) {
            queenPositions = new ArrayList<>();
        }

        public int hashCode() {
            return Objects.hashCode(queenPositions);
        }

        public boolean equals(Object o1) {
            if (o1 == null || o1.getClass() != Board.class) return false;
            else if (this == o1) return true;
            Board that = (Board) o1;
            return this.queenPositions == that.queenPositions;
        }
    }

    class Coordinate {
        int x;
        int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
