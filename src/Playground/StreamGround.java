package Playground;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StreamGround {

    public static void main(String[] args) {
        StreamGround program = new StreamGround();
        program.run();
    }

    public void run() {
        List<String> fruits = new ArrayList<>();
        fruits.add("apple");
        fruits.add("toast");
        fruits.add("orange");
        fruits.add("apricot");
        fruits.add("orangid");
        fruits.add("tangerine");

        List<Character> fruitTypes = fruits.stream().map(fruit -> fruit.charAt(0)).distinct().collect(Collectors.toList());

        for (Character type : fruitTypes) System.out.println(type);

        int[] numbers = new int[] {1,2,3,4,5,6,7,8,5,4,3,2};
        System.out.println(Arrays.stream(numbers).sum());
    }


}
