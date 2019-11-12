package LeetCode;

public class DiagonalTraverse {

    public static void main(String[] args) {
        DiagonalTraverse solution = new DiagonalTraverse();
        int[] result = solution.findDiagonalOrder(new int[][] {{1,2,3}, {4,5,6}, {7,8,9}});
        for (int num : result) System.out.println(num);
    }

    public int[] findDiagonalOrder(int[][] matrix) {
        if (matrix.length == 0) return new int[0];
        boolean up = true;
        int[] ans = new int[matrix.length * matrix[0].length];
        int ansPointer = 0;

        for (int i = 0; i < matrix.length + matrix[0].length - 1; i++) { //
            if (up) {
                int row = i < matrix.length ? i : matrix.length - 1;
                int col = i < matrix.length ? 0 : i - matrix.length + 1;

                while (row >= 0 && col < matrix[0].length) {
                    ans[ansPointer++] = matrix[row][col];
                    row--;
                    col++;
                }
            } else {
                int row = i < matrix[0].length ? 0 : (i+1) - matrix[0].length;
                int col = i < matrix[0].length ? i : matrix[0].length -1;

                while (row < matrix.length && col >= 0) {
                    ans[ansPointer++] = matrix[row][col];
                    row++;
                    col--;
                }
            }
            up = !up;
        }
        return ans;
    }
}
