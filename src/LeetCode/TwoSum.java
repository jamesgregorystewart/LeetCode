package LeetCode;

import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public static void main(String[] args) {

    }

    /*
    * Idea: map the values and indices. On iteration check to see if the target-num is key in the map
    * -> return the indices of num and target-num
    *
    * O(N)
    * */

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>(); //map val to index
        int[] ans = new int[2];

        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                ans[0] = map.get(target-nums[i]);
                ans[1] = i;
            } else {
                map.put(nums[i], i);
            }
        }

        return ans;
    }
}
