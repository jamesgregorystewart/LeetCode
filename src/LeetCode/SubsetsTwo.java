package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class SubsetsTwo {

    public static void main(String[] args) {
        SubsetsTwo solution = new SubsetsTwo();
        System.out.println(solution.subsetsWithDup(new int[] {1,2,2}));
    }

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(result, new ArrayList<>(), nums, 0);
        return result;
    }

    public void backtrack(List<List<Integer>> result, List<Integer> tempList, int[] nums, int start) {
        if (!result.contains(tempList)) result.add(new ArrayList<>(tempList));
        for (int i = start; i < nums.length; i++) {
            tempList.add(nums[i]);
            backtrack(result, tempList, nums, start + 1);
            tempList.remove(tempList.size() - 1);
        }
    }
}
