package LeetCode;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class MaxConferenceRooms {

    public static void main(String[] args) {
        MaxConferenceRooms solution = new MaxConferenceRooms();
        System.out.println(solution.maxConferenceRooms(new int[][] {{1,3},{2,6},{2,5},{5,7},{8,10},{15,18}}));
    }

    /*
    * Need to calculate how many conference rooms are required given a 2d array of meetings
    *
    * {1,3},{3,5} would be 1 as ending and starting at the same time does not mean overlap
    *
    * [[1,3],[2,6],[5,7],[8,10],[15,18]]
    *
    * max = 2
    *
    * 2,6
    * 5,7
    *
    * Idea:
    * - Create meeting objects
    * - Put into priority queue
    * */

    public int maxConferenceRooms(int[][] meetings) {
        int max = 0;
        //sort the meetings in ascending order by start time
        Arrays.sort(meetings, new Comparator<int[]>() {
           @Override
           public int compare(int[] o1, int[] o2) {
               return o1[0] - o2[0];
           }
        });
        PriorityQueue<int[]> q = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0]; //max heap on end time
            }
        });

        for (int[] meeting : meetings) {
            max = Math.max(max, q.size());
            while (!q.isEmpty() && q.peek()[1] <= meeting[0]) q.poll();
            q.offer(meeting);
        }
        max = Math.max(max, q.size());

        return max;
    }
}
