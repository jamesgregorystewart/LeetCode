package Playground;

import java.util.*;

public class playground {

    public static void main(String[] args) {

        playground program = new playground();
        program.run();
    }

    public void run() {
        String str = "and";
        for (int i = 0; i < str.length(); i++) {
            System.out.println(str.substring(0, i) + str.substring(i+1));
        }
    }
}
