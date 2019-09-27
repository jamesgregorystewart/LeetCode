//import java.util.ArrayDeque;
//import java.util.List;
//import java.util.Queue;
//
//class NumberOfIslands {
//
//    int numIslands = 0;
//
//    private class Coordinate {
//        public Integer x;
//        public Integer y;
//
//        public Coordinate(Integer x, Integer y) {
//            this.x = x;
//            this.y = y;
//        }
//    }
//
//    public int numIslands(char[][] grid) {
//        for (int i = 0; i < grid.length; i++) {
//            for (int j = 0; j < grid[i].length; j++) {
//                if (grid[i][j] == '1') {
//                    sink(grid, i, j);
//                    numIslands++;
//                }
//            }
//        }
//        return numIslands;
//    }
//
//    public void sink(char[][] grid, int row, int col) {
//        Queue<Coordinate> q = new ArrayDeque<>();
//        q.add(new Coordinate(row, col));
//
//        while (!q.isEmpty()) {
//            Coordinate cur = q.element();
//
//            for (Coordinate next : List.of(new Coordinate(cur.x+1, cur.y),
//                    new Coordinate(cur.x-1, cur.y),
//                    new Coordinate(cur.x, cur.y+1),
//                    new Coordinate(cur.x, cur.y-1))) {
//                if (next.x < 0 | next.x > grid.length | next.y < 0 | next.y > grid[0].length |
//                        grid[next.x][next.y] == '0') {
//                    continue;
//                }
//                grid[next.x][next.y] = '0';
//                q.add(grid[next.x][next.y]);
//            }
//            q.remove();
//        }
//    }
//}