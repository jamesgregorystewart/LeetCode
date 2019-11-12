package LeetCode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MinimumAreaRectangle {

    public static void main(String[] args) {
        MinimumAreaRectangle solution = new MinimumAreaRectangle();
//        System.out.println(solution.minAreaRect(new int[][]{{1,1},{1,3},{3,1},{3,3},{2,2}}));
    }

    int minArea = 0;

//    public int minAreaRect(int[][] points) {
//        Map<Integer, ArrayList<Integer>> x_points = new HashMap<>();
//        Map<Integer, ArrayList<Integer>> y_points = new HashMap<>();
//        //O(N)
//        for (int[] point : points) {
//            x_points.getOrDefault(point[0], new ArrayList<>()).add(point[1]);
//            y_points.getOrDefault(point[1], new ArrayList<>()).add(point[0]);
//        }
//
//        for (int x_point : x_points.keySet()) {
//            if (x_points.get(x_point).size() >= 2) {
//                List<Integer> y_vals = new ArrayList<>(x_points.get(x_point));
//                // O(K^2) where K is the unique y_points with x_val == x_point
//                for (int i = 0; i < y_vals.size()-1; i++) {
//                    for (int j = i+1; j < y_vals.size(); j++) {
//                        calcMinArea(y_points, i, j);
//                    }
//                }
//            }
//        }
//        return minArea;
//    }

    public void calcMinArea(HashMap<Integer, ArrayList<Integer>> y_points, int i, int j) {

    }
}
