package LeetCode;

import java.util.Arrays;

public class ArrayPartitionI {

    public static void main(String[] args) {
        ArrayPartitionI solution = new ArrayPartitionI();
        System.out.println(solution.arrayPairSum(new int[] {}));
    }

    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int result = 0;

        for (int i = 0; i < nums.length-1; i+=2) {
            result += Math.min(nums[i], nums[i+1]);
        }
        return result;
    }
}
