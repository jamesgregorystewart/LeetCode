//package Playground;
//
//import java.util.Arrays;
//import java.util.HashMap;
//
//public class Battleship {
//
//    public static void main(String[] args) {
//        Battleship battleship = new Battleship();
//        battleship.init();
//    }
//
//    HashMap<Integer, Integer> ships;
//    int[][] yourGrid;
//    int[][] theirGrid;
//
//    public void init() {
//
//        Arrays.fill(grid, -1);
//
//        //these are the different boats
//        this.ships = new HashMap<>();
//        ships.put(1, 2); //1 is cruiser
//        ships.put(2, 3); // 2 is destroyer
//        ships.put(3, 4); // 3 is submarine
//        ships.put(4, 4); // 4 is battlship
//        ships.put(5, 5); // 5 is aircraft carrier
//    }
//
//    private void hit(Coordinate coord) {
//        int ship = grid[coord.y][coord.x];
//        if (ship == -1) {
//            System.out.println("HA you missed!");
//            grid[coord.y][coord.x] = 0;
//        }
//        yourGrid.put(ship, map.get(val) -1);
//        if (yourGrid.get(ship) == 0) {
//            System.out.println("you hit " + val);
//        }
//    }
//
//    class Coordinate {
//        int x;
//        int y;
//    }
//}
