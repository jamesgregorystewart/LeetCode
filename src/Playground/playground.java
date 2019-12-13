package Playground;

import java.util.*;

public class playground {

    public static void main(String[] args) {

        playground program = new playground();
        program.run();
    }

    public void run() {

        PriorityQueue<Coordinate> q = new PriorityQueue<>(new Comparator<Coordinate>() {
            @Override
            public int compare(Coordinate o1, Coordinate o2) {
                return 0;
            }
        });

//        System.out.println(0 == 0.0);

        new Thread() {
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(1000);
                        System.out.println("you're awesome");
                    } catch (InterruptedException e) {
                        System.out.println("Thread interrupted.");
                    }
                }
            }
        }.start();
        try {
            Thread.sleep(500);
        } catch(InterruptedException e) {
            System.out.println(e.getMessage());
        }
        new Thread() {
            public void run() {
                while (true) {
                    try {
                        Thread.sleep(1000);
                        System.out.println("No, YOUR'RE awesome!");
                    } catch (InterruptedException e) {
                        System.out.println("Thread interrupted.");
                    }
                }
            }
        }.start();

    }

    class Coordinate implements Comparable<Coordinate> {
        int x;
        int y;

        @Override
        public int compareTo(Coordinate o) {
            return 0;
        }
    }
}
