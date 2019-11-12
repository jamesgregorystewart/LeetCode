package LeetCode;

public class MaximumProductSubarray {

    public static void main(String[] args) {
        MaximumProductSubarray solution = new MaximumProductSubarray();
        System.out.println(solution.maxProduct(new int[] {-2,0,1,-3}));
    }

    /*
    * Strategy: Calculate the product from the left and the right and find the max between both halves
    * */

    public int maxProduct(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int max = nums[0];
        int minProd = nums[0];
        int maxProd = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int n = minProd * nums[i];
            int m = maxProd * nums[i];

            minProd = Math.min(nums[i], Math.min(n, m));
            maxProd = Math.max(nums[i], Math.max(n, m));

            max = Math.max(max, maxProd);
        }
        return max;
    }
}
