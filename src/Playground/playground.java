package Playground;

public class playground {

    public static void main(String[] args) {
        String test = "1,2,null,null,3,null,null,4,5,";
        String[] testArr = test.split(",");
        for (String str : testArr) {
            System.out.println(str + " <<");
        }
    }
}
