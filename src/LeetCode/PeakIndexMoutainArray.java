package LeetCode;

public class PeakIndexMoutainArray {

    public static void main(String[] args) {
        PeakIndexMoutainArray solution = new PeakIndexMoutainArray();
        System.out.println(solution.peakIndexInMountainArray(new int[] {0,1,0}));
    }

    public int peakIndexInMountainArray(int[] A) {
        if (A.length == 0 || A.length == 1) return 0;

        for (int i = 0; i < A.length; i++) {
            if (i == 0) {
                if (A[i] > A[i+1]) return 0;
            }
            else if (i == A.length-1) {
                if (A[i-1] < A[i]) return A.length-1;
            }
            else if (A[i-1] < A[i] && A[i] > A[i + 1]) return i;

        }
        return 0; //check this
    }
}
