package LeetCode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class SpiralMatrix {

    public static void main(String[] args) {
        SpiralMatrix solution = new SpiralMatrix();
        List<Integer> result = solution.spiralOrder(new int[][] {{1,2,3,10}, {4,5,6,11}, {7,8,9,12}});
        for (int num : result) System.out.println(num);
    }

    /*
    * Idea: track which direction we are going;
    *       maintain visited hashset to track whether we have visited the given coordinate.
    *       -> if so then switch to the next direction
    * */

    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0) return new ArrayList<>();
        int N = matrix.length * matrix[0].length;
        List<Integer> res = new ArrayList<>();
        boolean[][] seen = new boolean[matrix.length][matrix[0].length];
        int count = 0;
        int direction = 0; // 0 == right; 1 == down; 2 == left; 3 == up;
        int row = 0;
        int col = 0;

        while (count < N) {
            if (!seen[row][col]) {
                res.add(matrix[row][col]);
                count++;
            }
            seen[row][col] = true;
            if (direction == 0) {
                if (col == matrix[0].length -1 || seen[row][col+1]) {
                    direction = 1;
                    row++;
                }
                else col++;
            } else if (direction == 1) {
                if (row == matrix.length - 1 || seen[row+1][col]) {
                    direction = 2;
                    col--;
                }
                else row++;
            } else if (direction == 2) {
                if (col == 0 || seen[row][col-1]) {
                    direction = 3;
                    row--;
                }
                else col--;
            } else {
                if (row == 0 || seen[row-1][col]) {
                    direction = 0;
                    col++;
                }
                else row--;
            }
        }
        return res;
    }
}
