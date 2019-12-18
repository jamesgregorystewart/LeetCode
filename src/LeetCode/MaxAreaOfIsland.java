package LeetCode;

import java.util.*;

public class MaxAreaOfIsland {

    public static void main(String[] args) {
        MaxAreaOfIsland solution = new MaxAreaOfIsland();
        int[][] grid0 = new int[][] {{1,1,1,1,1},{1,1,1,1,1}};
        int[][] grid = new int[][] {{0,0,1,0,0,0,0,1,0,0,0,0,0},
                                    {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                    {0,1,1,0,1,0,0,0,0,0,0,0,0},
                                    {0,1,0,0,1,1,0,0,1,0,1,0,0},
                                    {0,1,0,0,1,1,0,0,1,1,1,0,0},
                                    {0,0,0,0,0,0,0,0,0,0,1,0,0},
                                    {0,0,0,0,0,0,0,1,1,1,0,0,0},
                                    {0,0,0,0,0,0,0,1,1,0,0,0,0}};
        System.out.println(solution.maxAreaOfIsland(grid0));
    }

    /*
    * Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

    Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

    Example 1:

    [[0,0,1,0,0,0,0,1,0,0,0,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,1,1,0,1,0,0,0,0,0,0,0,0],
     [0,1,0,0,1,1,0,0,1,0,1,0,0],
     [0,1,0,0,1,1,0,0,1,1,1,0,0],
     [0,0,0,0,0,0,0,0,0,0,1,0,0],
     [0,0,0,0,0,0,0,1,1,1,0,0,0],
     [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
    Example 2:

    [[0,0,0,0,0,0,0,0]]
    Given the above grid, return 0.
    Note: The length of each dimension in the given grid does not exceed 50.
    *
    * */
    int rows;
    int cols;
    int[][] grid;

    public int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        rows = grid.length;
        cols = grid[0].length;
        this.grid = grid;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 1) max = Math.max(calcArea(new Coordinate(j, i)), max);
            }
        }

        return max;
    }

    private int calcArea(Coordinate coord) {
        int runningArea = 1;
        LinkedList<Coordinate> toInspect = new LinkedList<>();
        toInspect.add(coord);
        while (!toInspect.isEmpty()) {
            Coordinate curr = toInspect.removeFirst();
            grid[curr.y][curr.x] = 0;
            List<Coordinate> surrounding = new ArrayList<>();
            surrounding.add(new Coordinate(curr.x, curr.y+1));
            surrounding.add(new Coordinate(curr.x, curr.y-1));
            surrounding.add(new Coordinate(curr.x+1, curr.y));
            surrounding.add(new Coordinate(curr.x-1, curr.y));
            for (Coordinate c : toInspect) System.out.println("toInspect: " + c.x + " " + c.y);
            for (Coordinate next: surrounding) {
                if (next.x >= 0 && next.x < cols && next.y >= 0 && next.y < rows && grid[next.y][next.x] == 1) {
                    grid[next.y][next.x] = 0;
                    toInspect.add(next);
                    runningArea++;
                    System.out.println("coord: " + next.x + "," + next.y);
                }
            }
        }

        return runningArea;
    }

    class Coordinate {
        int x;
        int y;

        Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
