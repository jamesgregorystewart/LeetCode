package LeetCode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class NumberOfIslands {

    public static void main(String[] args) {
        NumberOfIslands solution = new NumberOfIslands();
        System.out.println(solution.numIslands(new char[][] {{'1','1','1','1','0'},
                {'1','1','0','1','0'},
                {'1','1','0','0','0'},
                {'0','0','0','0','1'}}));
    }

    /*
    * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Example 1:

    Input:
    11110
    11010
    11000
    00000

    Output: 1
    Example 2:

    Input:
    11000
    11000
    00100
    00011

    Output: 3
    * */

    public int numIslands(char[][] grid) {
        int islands = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    sink(grid, i, j);
                    islands++;
                }
            }
        }
        return islands;
    }

    //DFS approach -> stack
    public void sink(char[][] grid, int row, int col) {
        Stack<Coordinate> stack = new Stack<>();
        Coordinate root = new Coordinate(col, row);
        stack.add(root);
        while (!stack.isEmpty()) {
            Coordinate curr = stack.pop();
            grid[curr.y][curr.x] = '0';
            List<Coordinate> adj = new ArrayList<>();
            adj.add(new Coordinate(curr.x+1, curr.y));
            adj.add(new Coordinate(curr.x-1, curr.y));
            adj.add(new Coordinate(curr.x, curr.y+1));
            adj.add(new Coordinate(curr.x, curr.y-1));
            for (Coordinate next : adj) {
                if (isInBounds(grid, next) && grid[next.y][next.x] == '1') stack.push(next);
            }
        }
    }

    public boolean isInBounds(char[][] grid, Coordinate coord) {
        return coord.x >= 0 && coord.x < grid[0].length && coord.y >= 0 && coord.y < grid.length;
    }

    class Coordinate {
        int x;
        int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
