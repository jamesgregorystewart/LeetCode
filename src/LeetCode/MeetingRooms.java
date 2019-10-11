package LeetCode;

import java.util.*;

public class MeetingRooms {

    public static void main(String[] args) {
        MeetingRooms solution = new MeetingRooms();
        System.out.println(solution.minMeetingRooms(new int[][] {{}}));
    }

    public int minMeetingRooms(int[][] intervals) {

        if (intervals.length == 0 || intervals[0].length == 0) return 0;

        PriorityQueue<Integer> rooms = new PriorityQueue<>(); //this will automatically put in ascending order
        Arrays.sort(intervals, (m1, m2) -> m1[0] - m2[0]);

        rooms.add(intervals[0][1]);

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] >= rooms.peek()) { // meeting can be assigned to an existing room
                rooms.poll();
            }
            rooms.add(intervals[i][1]);
        }
        return rooms.size();
    }
}
