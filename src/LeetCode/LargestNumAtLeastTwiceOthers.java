package LeetCode;

public class LargestNumAtLeastTwiceOthers {

    public static void main(String[] args) {
        LargestNumAtLeastTwiceOthers solution = new LargestNumAtLeastTwiceOthers();
        System.out.println(solution.dominantIndex(new int[] {48,57,6,80,29,55,97,4,26,29,41,28,84,54,89,1,85,11,90,47,37,50,0,96,44,64,42,41,64,62,61,52,57,10,44,78,20,23,38,56,81,5,56,40,81,40,56,17,97,16}));
    }

    /*
    * Approach: store max on first iteration then loop through again and find largest num that isn't
    * */

    public int dominantIndex(int[] nums) {
        if (nums.length == 1) return 0;

        int largest;
        int largest_idx;
        int penultimate;
        largest = nums[0]; largest_idx = 0;
        penultimate = largest;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == 16) {
                int x = 0;
            }
            if (nums[i] > largest) {
                penultimate = largest;
                largest = nums[i];
                largest_idx = i;
            } else if (penultimate == largest && nums[i] != largest) penultimate = nums[i];
            else if (largest != nums[i]) penultimate = Math.max(penultimate, nums[i]);
        }

        return largest >= 2 * penultimate ? largest_idx : -1;
    }
}
