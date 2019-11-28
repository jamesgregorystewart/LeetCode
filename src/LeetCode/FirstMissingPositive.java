package LeetCode;

public class FirstMissingPositive {

    public static void main(String[] args) {
        FirstMissingPositive solution = new FirstMissingPositive();
        System.out.println(solution.firstMissingPositive(new int[] {1,1,1,1,1}));
    }

    /*
    * Given an unsorted integer array, find the smallest missing positive integer.
    *

        Example 1:

        Input: [1,2,0]
        Output: 3

        Example 2:

        Input: [3,4,-1,1]
        Output: 2
        Example 3:

        Input: [7,8,9,11,12]
        Output: 1
        Note:

        Your algorithm should run in O(n) time and use constant extra space.

    Procedure:
    1) Preprocess anything less than 0 to 0 and anything greater than size to 0
    2) recursively iterate and rearrange the values

    * */

    public int firstMissingPositive(int[] nums) {

        //preprocess
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] < 0 || nums[i] > nums.length ? 0 : nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == i+1) nums[i] = -1;
            else if (nums[i] == -1) continue;
            else if (nums[i] != i+1 && nums[i] != 0) swap(nums, i);
        }

        // -1 -> 1
        for (int i = 0; i < nums.length; i++) {
            nums[i] = nums[i] == -1 ? 1 : nums[i];
        }

        int ans = nums.length+1;
        //post-process
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                ans = i+1;
                break;
            }
        }

        return ans;
    }

    private void swap(int[] nums, int i) {
        int idx = nums[i]-1; //location of what to make '1'
        nums[i] = 0;
        if (nums[idx] == -1) return;
        if (nums[idx] != 0) swap(nums, idx);
        nums[idx] = -1;
    }
}
