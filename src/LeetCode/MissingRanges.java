package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class MissingRanges {
//2147483647
    public static void main(String[] args) {
        MissingRanges solution = new MissingRanges();
        List<String> result = solution.findMissingRanges(new int[] {}, 0, 2147483647);
        for (String str : result)
            System.out.println(str);
    }


    public List<String> findMissingRanges(int[] nums, int lower, int upper) {

        List<String> result = new ArrayList<>();

        int i = 0;
        while (lower <= upper && i < nums.length) {
            if (lower < nums[i]) {
                if (nums[i]-lower == 1) {
                    result.add((lower)+"");
                    lower+=2;
                }
                else {
                    result.add(lower + "->" + (nums[i] - 1));
                    if (nums[i] == Integer.MAX_VALUE) return result;
                    lower = nums[i] + 1;
                }
            }
            else if (lower == nums[i]) {
                if (nums[i] == Integer.MAX_VALUE) return result;
                lower++;
            }
            i++;
        }

        if (lower <= upper) {
            if (upper == lower)
                result.add(lower + "");
            else
                result.add(lower + "->" + upper);
        }

        return result;
    }
}
