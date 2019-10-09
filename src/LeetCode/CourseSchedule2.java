package LeetCode;

import java.awt.*;
import java.util.*;
import java.util.List;

public class CourseSchedule2 {

    enum COLOR {
        WHITE,
        BLACK,
        GRAY
    }
    boolean isPossible;

    public static void main(String[] args) {
        CourseSchedule2 solution = new CourseSchedule2();
        solution.isPossible = true;
        int[] result = solution.findOrder(2, new int[][] {{}});
        for (int course : result)
            System.out.println(course);
    }

    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> courses = new HashMap<>(); //this is what we will traverse through;
        Stack<Integer> done = new Stack<>(); //the courses we are finished looking at
        HashMap<Integer, COLOR> color = new HashMap<>();

        //first load up the courses
        int leftOff = 0;
        for (int i = 0; i < prerequisites.length; i++, leftOff++) {
            if (prerequisites[i].length == 0) break;
            courses.putIfAbsent(prerequisites[i][1], new ArrayList<>());
            courses.putIfAbsent(prerequisites[i][0], new ArrayList<>());
            color.put(prerequisites[i][0], COLOR.WHITE);
            color.put(prerequisites[i][1], COLOR.WHITE);
            courses.get(prerequisites[i][1]).add(prerequisites[i][0]);
        }
        for (int i = 0; i < numCourses; i++) {
            courses.putIfAbsent(i, new ArrayList<>());
            color.put(i, COLOR.WHITE);
        }

        //traverse the map
        for (Map.Entry<Integer, List<Integer>> prerequisite : courses.entrySet()) {
            if (color.get(prerequisite.getKey()) == COLOR.WHITE) {
                dfs(prerequisite.getKey(), courses, color, done);
            }
        }

        //create the returned list of ints
        int[] result;
        int pointer = 0;
        if (this.isPossible) {
            result = new int[numCourses];
            while (!done.isEmpty()) {
                int course = done.pop();
                result[pointer++] = course;
            }
        } else
            result = new int[0];
        return result;
    }

    public void dfs(Integer cur, Map<Integer, List<Integer>> courses, HashMap<Integer, COLOR> color, Stack<Integer> done) {
        if (!this.isPossible) return; // a cycle has been found

        color.put(cur, COLOR.GRAY);

        for (Integer course : courses.get(cur)) {
            if (color.get(course) == COLOR.WHITE)
                dfs(course, courses, color, done);
            else if (color.get(course) == COLOR.GRAY)
                this.isPossible = false;

        }
        done.push(cur);
        color.put(cur, COLOR.BLACK);
    }
}
