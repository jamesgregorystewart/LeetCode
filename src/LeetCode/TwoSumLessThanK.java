package LeetCode;

public class TwoSumLessThanK {

    public static void main(String[] args) {
        TwoSumLessThanK solution = new TwoSumLessThanK();
        System.out.println(solution.twoSumLessThanK(new int[] {34,23,1,24,75,33,54,8}, 60));
    }

    public int twoSumLessThanK(int[] A, int K) {
        if (A.length == 1) return -1;

        int maxSum = -1;
        for (int i = 0; i < A.length-1; i++) {
            for (int j = i+1; j < A.length; j++) {
                if (A[i] + A[j] < K) maxSum = Math.max(maxSum, A[i] + A[j]);
            }
        }

        return maxSum;
    }
}
