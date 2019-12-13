package LeetCode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Permutations {

    /*
    *Given a collection of distinct integers, return all possible permutations.

    Example:

    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    * */

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(nums, new ArrayList<>(), result, new HashSet<>());
        return result;
    }

    public void backtrack(int[] nums, List<Integer> tempList, List<List<Integer>> result, HashSet<Integer> seen) {
        if (tempList.size() == nums.length) result.add(new ArrayList<>(tempList));
        else {
            for (int i = 0; i < nums.length; i++) {
                if (!seen.contains(nums[i])) {
                    tempList.add(nums[i]);
                    seen.add(nums[i]);
                    backtrack(nums, tempList, result, seen);
                    int num = tempList.remove(tempList.size()-1);
                    seen.remove(num);
                }
            }
        }
    }
}
