package Playground;

import Utility.TreeDeserializer;
import Utility.TreeNode;

import java.util.*;

public class playground {

    public static void main(String[] args) {

        playground program = new playground();
        program.run();
    }

    enum COLOR {
        WHITE,
        GRAY,
        BLACK
    };

    public void run() {

        Map<Integer, COLOR> map = new HashMap<>();
        map.put(0, COLOR.WHITE);


//        TreeDeserializer treeDeserializer = new TreeDeserializer();
//        TreeNode root = treeDeserializer.deserialize(new String[] {"1", "3", "2", null, "4", null, "5"});

        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(6);
        list.add(5);
        list.add(4);
        System.out.println(list);
        Collections.sort(list);
        System.out.println(list);

        char c = '3';
        System.out.println(c - '0');
    }

}
