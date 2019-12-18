package LeetCode;

import java.util.*;
import java.util.List;

public class MergeIntervals {

    public static void main(String[] args) {
        MergeIntervals solution = new MergeIntervals();
        //{1,3},{2,6},{8,10},{15,18}
        int[][] result = solution.merge(new int[][] {{1,3},{2,6},{8,10},{15,18}});
        for (int[] interval : result) {
            System.out.println(interval[0] + " " + interval[1]);
        }
    }

    /*
    * Given a collection of intervals, merge all overlapping intervals.

    Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
    Example 2:

    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
    *
    * */

    //TODO: Do a max overlap problem like this but counting max at same time -> would be equivalent to "how many conference rooms are needed to
    //schedule all meetings

    public int[][] merge(int[][] intervals) {
        if (intervals.length == 0) return new int[][] {{}};
        List<int[]> mergedIntervals = new ArrayList<>();
        //sort intervals in order of their start time
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        //process intervals
        int[] curr = intervals[0];
        if (intervals.length == 1) mergedIntervals.add(curr);

        for (int[] interval : intervals) {
            if (curr == null) curr = interval;
            //merge intervals
            if (interval[0] <= curr[1]) {
                System.out.println("end point "+curr[1]+" updating to "+interval[1]);
                curr[1] = interval[1];
            }
            //have a finished interval
            else {
                System.out.println("saving ["+curr[0]+","+curr[1]+"]");
                System.out.println("updating curr to ["+interval[0]+","+interval[1]+"]");
                mergedIntervals.add(curr);
                curr = interval;
            }
        }
        if (mergedIntervals.size() == 0 ||
                mergedIntervals.get(mergedIntervals.size()-1)[1] != curr[1])
            mergedIntervals.add(curr);

        //put answer into return format
        int[][] ans = new int[mergedIntervals.size()][2];
        int idx = 0;
        for (int[] interval : mergedIntervals) {
            ans[idx][0] = interval[0];
            ans[idx++][1] = interval[1];

        }
        return ans;
    }
}
