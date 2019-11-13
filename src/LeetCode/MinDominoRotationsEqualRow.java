package LeetCode;

public class MinDominoRotationsEqualRow {

    public static void main(String[] args) {
        MinDominoRotationsEqualRow solution = new MinDominoRotationsEqualRow();
        System.out.println(solution.minDominoRotations(new int[] {3,5,1,2,3}, new int[] {3,6,3,3,4}));
    }

    /*
    * Approach: count and maintain max sum for A and B; return dominoes.length-the highest max
    *
    *
    * */

    public int minDominoRotations(int[] A, int[] B) {
        int[] aCount = new int[7];
        int[] bCount = new int[7];
        int[] tCount = new int[7];
        int max = 0;
        int tMax = 0;

        //O(N) where N is the number of dominoes
        for (int i = 0; i < A.length; i++) {
            aCount[A[i]]++;
            max = Math.max(aCount[A[i]], max);
            bCount[B[i]]++;
            max = Math.max(bCount[B[i]], max);
            if (A[i] == B[i]) tCount[A[i]]++;
            else {
                tCount[A[i]]++;
                tCount[B[i]]++;
            }
            tMax = Math.max(tCount[A[i]], tMax);
            tMax = Math.max(tCount[B[i]], tMax);
        }

        if (tMax < A.length) return -1;
        return A.length - max;
    }
}
