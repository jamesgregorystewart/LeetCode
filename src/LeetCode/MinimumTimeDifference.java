package LeetCode;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MinimumTimeDifference {

    public static void main(String[] args) {
        MinimumTimeDifference solution = new MinimumTimeDifference();
//        System.out.println(solution.findMinDifference());
    }

    /*
    * Time: O(Nlog(N))
    * 1) Sort the list into ascending order
    * Need to standardize the times into a raw minute format when doing calculations
    * Need to perform two calculations with ever set of points ->
    *
    * */

    public int findMinDifference(List<String> timePoints) {

        int min = Integer.MAX_VALUE;
        Collections.sort(timePoints);

        //first check front and back
        min = Math.min(min, calcDifference(timePoints.get(0), timePoints.get(timePoints.size()-1)));
        //then iterate through checking adjacent times
        for (int i = 0; i < timePoints.size()-1; i++) {
            min = Math.min(min, calcDifference(timePoints.get(i), timePoints.get(i+1)));
        }
        return min;
    }

    public int calcDifference(String s1, String s2) {
        int i1 = Integer.valueOf(s1.substring(0,2)) * 60 + Integer.valueOf(s1.substring(3));
        int i2 = Integer.valueOf(s2.substring(0,2)) * 60 + Integer.valueOf(s2.substring(3));

        return Math.min(24*60 + i1 - i2 ,Math.abs(i1 - i2));
    }
}
