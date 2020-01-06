package LeetCode;

public class Search2DMatrixIIB {

    public static void main(String[] args) {
        Search2DMatrixIIB solution = new Search2DMatrixIIB();
        System.out.println(solution.searchMatrix(new int[][] {
        {1,4,7, 11, 15},
        {2,   5,  8, 12, 19},
        {3,   6,  9, 16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}}, 5));
    }

    /*
    * Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    Example:

    Consider the following matrix:

    [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    Given target = 5, return true.

    Given target = 20, return false.
    * */

    /*
    * Idea: binary search for the row and column
    *
    * TODO: did this whole problem incorrectly. I presumed this was similar to the first verision of this problem
    * */

    public boolean searchMatrix(int[][] matrix, int target) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        if (target < matrix[0][0] || target > matrix[rows-1][cols-1]) return false;
        int row = findRow(matrix, target);
        System.out.println(row);
        int col = findColumn(matrix, row, target);
        System.out.println(col);
        return target == matrix[row][col];
    }

    /*
    * Need to use the concept of checking current and the next index
    * - <= left and right and right will be set to mid and left will be set to mid + 1
    * */
    public int findRow(int matrix[][], int target) {
        int top = 0;
        int bottom = matrix.length - 1;
        int mid = top + (bottom - top) / 2;
        while (top < bottom) {
            mid = top + (bottom - top) / 2;
            if (mid == matrix.length-1 || (target >= matrix[mid][0] && target < matrix[mid+1][0]))
                return mid;
            else if (target < matrix[mid][0]) {
                bottom = mid;
            } else {
                top = mid + 1;
            }
        }
        return mid; //okay to return the wrong value here
    }

    public int findColumn(int matrix[][], int row, int target) {
        int left = 0;
        int right = matrix[row].length;
        int mid = left + (right - left) / 2;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (target == matrix[row][mid]) {
                return mid;
            } else if (target < matrix[row][mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return mid; //okay to return the wrong value here
    }
}






