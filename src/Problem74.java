class Problem74 {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null) return false;
        if (target < matrix[0][0] || target > matrix[matrix.length-1][matrix[0].length-1]) {
            return false;
        }

        //swap out row and col for the calls to binary search when completed
        int row = searchRow(matrix, 0, matrix.length-1, target);
        int col = searchCol(matrix, row, 0, matrix[0].length-1, target);
        System.out.println(row);
        System.out.println(col);
        if (matrix[row][col] != target) return false;
        return true;
    }

    private int searchRow(int[][] matrix, int front, int back, int target) {
        int mid = (front + back) / 2;
        if (front >= back || (target >= matrix[mid][0] && target < matrix[mid+1][0])) return mid;
        else if (target < matrix[mid][0]) searchRow(matrix, front, mid, target);
        else if (target > matrix[mid][0]) searchRow(matrix, mid, back, target);

        return mid;
    }

    private int searchCol(int[][] matrix, int row, int front, int back, int target) {
        int mid = (front + back) / 2;

        if (front >= back || (target >= matrix[row][mid] && target < matrix[mid+1][0])) return mid;
        else if (target < matrix[row][mid]) searchCol(matrix, row, front, mid, target);
        else if (target > matrix[row][mid]) searchCol(matrix, row, mid, back, target);

        return mid;
    }
}