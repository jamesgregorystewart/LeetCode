package LeetCode;

import java.util.PriorityQueue;

public class KClosestPointsToOrigin {

    public static void main(String[] args) {
        KClosestPointsToOrigin solution = new KClosestPointsToOrigin();
        int[][] ans = solution.kClosest(new int[][] {{3,3},{5,-1},{-2,4}}, 2);
        for (int[] coord : ans) {
            System.out.println(coord[0] + " " + coord[1]);
        }
    }

    public int[][] kClosest(int[][] points, int K) {

        PriorityQueue<Coordinate> queue = new PriorityQueue<>();

        for (int[] point : points) {
            queue.add(new Coordinate(point[0], point[1]));
        }

        if (queue.size() < K) return new int[][] {{}};

        int [][] ans = new int[K][];
        for (int i = 0; i < K; i++) {
            Coordinate coord = queue.poll();
            ans[i] = new int[] {coord.x, coord.y};
        }

        return ans;
    }

    class Coordinate implements Comparable<Coordinate> {
        int x;
        int y;
        double eucDist;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
            this.eucDist = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
        }

        @Override
        public int compareTo(Coordinate coordinate) {
            if (this.eucDist < coordinate.eucDist) return -1;
            else return 1;
        }
    }
}
