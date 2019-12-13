package LeetCode;

import java.util.Arrays;

public class IncreasingTripletSubsequence {

    public static void main(String[] args) {
        IncreasingTripletSubsequence solution = new IncreasingTripletSubsequence();
        System.out.println(solution.increasingTriplet(new int[] {2,1,5,0,4,6}));
    }

    /*
    * Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

    Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
    Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.
    * */

    public boolean increasingTriplet(int[] nums) {
        if (nums.length < 3) return false;

        int[] seq = new int[3];
        Arrays.fill(seq, -1);
        seq[0] = nums[0];
        boolean minSet = false;
        boolean midSet = false;


        for (int i = 1; i < nums.length; i++) {
            if (minSet) {

            }
            if (nums[i] < seq[0]) {
                seq[0] = nums[i];
            } else
                minSet = true;

            if (i < nums.length-2 && nums[i + 1] > nums[i]) {
                if (i < nums.length-2 && nums[i+2] > nums[i + 1])
                    return true;
            }
        }

        return false;
    }
}
