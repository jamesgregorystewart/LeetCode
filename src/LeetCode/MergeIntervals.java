//package LeetCode;
//
//import java.util.*;
//import java.util.List;
//
//public class MergeIntervals {
//
//    public static void main(String[] args) {
//        MergeIntervals solution = new MergeIntervals();
//        //{1,3},{2,6},{8,10},{15,18}
//        int[][] result = solution.merge(new int[][] {{1,4},{4,5}});
//        for (int[] interval : result) {
//            System.out.println(interval[0] + " " + interval[1]);
//        }
//    }
//
//    public int[][] merge(int[][] intervals) {
//        if (intervals.length == 0 || intervals[0].length == 0) return new int[][] {{}};
//
//        Comparator<int[]> comparator = new Comparator<int[]>() {
//            @Override
//            public int compare(int[] o1, int[] o2) {
//                if (o1[0] < o2[0]) return -1;
//                return 0;
//            }
//        };
//
//        Arrays.sort(intervals, comparator);
//        List<List<Integer>> result = new ArrayList<>();
//
//        //O(N) where N = number of intervals to merge
//        boolean waiting = false;
//        List<Integer> interval;
//        int maxR;
//        for (int i = 0; i < intervals.length-1; i++) {
//            if (!waiting) {
//                interval = new ArrayList<>();
//                interval.add(intervals[i][0]);
//                if (intervals[i+1][0] > intervals[i][1]) {
//                    interval.add(intervals[i][1]);
//                } else waiting = true;
//                result.add(interval);
//            } else if (intervals[i+1][0] > intervals[i][1]) { //stop waiting and finish the interval
//                result.get(result.size()-1).add(intervals[i][1]);
//                waiting = false;
//            }
//        }
//
//        //waiting for the last range digit to complete
//        else if (result.size() > 0 && result.get(result.size()-1).size() == 1) {
//            if (intervals[intervals.length-1][1] < intervals[intervals.length-2][1])
//                result.get(result.size()-1).add(intervals[intervals.length-2][1]);
//            result.get(result.size()-1).add(intervals[intervals.length-1][1]);
//        }
//        else {
//            List<Integer> tmp = new ArrayList<>();
//            tmp.add(intervals[intervals.length-1][0]);
//            tmp.add(intervals[intervals.length-1][1]);
//            result.add(tmp);
//        }
//
//        //O(N) to put into the return type
//        int[][] ans = new int[result.size()][2];
//        for (int i = 0; i < result.size(); i++) {
//            ans[i][0] = result.get(i).get(0);
//            ans[i][1] = result.get(i).get(1);
//        }
//        return ans;
//    }
//}
