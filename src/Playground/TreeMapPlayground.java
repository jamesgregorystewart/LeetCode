package Playground;

import java.util.Comparator;
import java.util.TreeMap;

public class TreeMapPlayground {

    public static void main(String[] args) {
        TreeMapPlayground treeMapPlayground = new TreeMapPlayground();
        treeMapPlayground.run();
    }

    public void run() {
        TreeMap<Integer, Integer> tree = new TreeMap<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return 1;
            }
        });

        TreeMap<Integer, Integer> map = new TreeMap<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return 0;
            }
        });
    }
}
