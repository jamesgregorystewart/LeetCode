package LeetCode;

public class MaximalSquare {

    /*
    * Idea: Iterate right -> left && top -> down so we will always approach square from the top left;
    *   After processing a '1' turn it into a '0'
    *   When a 1 is reached queue
    *
    * */

    int maxArea = 0;

    public int maximalSquare(char[][] matrix) {

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == '1') calcSquare(matrix, new int[] {i, j+1}, 2);
            }
        }
        return maxArea;
    }

    public void calcSquare(char[][] matrix, int[] start, int n) {
        maxArea = Math.max(maxArea, 1);
        int row = start[0] + (n-1);
        if (start[1] >= matrix[0].length || row >= matrix.length) return;

        //go down
        for (int i = start[0]; i < start[0] + n; i++) {
            if (matrix[i][start[1]] == '0') return;
        }

        //go left
        for (int i = start[1]; i >= start[1]-(n-1); i--) {
            if (matrix[row][i] == '0') return;
        }

        maxArea = Math.max(n * n, maxArea);
        start[1]++;
        calcSquare(matrix, start, n+1);
    }
}
