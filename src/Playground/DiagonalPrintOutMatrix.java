package Playground;

import java.util.ArrayList;
import java.util.List;

public class DiagonalPrintOutMatrix {

    public static void main(String[] args) {
        DiagonalPrintOutMatrix solution = new DiagonalPrintOutMatrix();
        List<List<Integer>> answer = solution.diagonalPrintOut(new int[][] {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}});
        for (List<Integer> diagonal : answer) {
            for (Integer e : diagonal) {
                System.out.println(e);
            }
            System.out.println("-----");
        }
    }

    public List<List<Integer>> diagonalPrintOut(int[][] matrix) {
        int N = matrix.length;
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < 2*N - 1; ++i) {

            //printing starting from the top row
            if (i < N) {
                int j = i; int k = 0; // j == column; k == row
                List<Integer> diagonal = new ArrayList<>();
                while (j >= 0) {
                    diagonal.add(matrix[k++][j--]);
                }
                result.add(diagonal);
            }

            //printing from the right side
            else {
                int j = N-1; int k = i - N + 1; // j == column; k == row
                List<Integer> diagonal = new ArrayList<>();
                while (k < N) {
                    diagonal.add(matrix[k++][j--]);
                }
                result.add(diagonal);
            }
        }
        return result;
    }
}
