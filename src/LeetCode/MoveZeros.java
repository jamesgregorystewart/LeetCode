package LeetCode;

public class MoveZeros {

    /*
    * Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:

    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
    * */

    public static void main(String[] args) {
        MoveZeros solution = new MoveZeros();
        int[] values = new int[] {0,1,0,3,12};
        solution.moveZeroes(values);
        for (int num : values) {
            System.out.println(num);
        }
    }

    public void moveZeroes(int[] nums) {
        int offset = 0; //increment this whenever a 0 is replaced
        for (int i = 0; i < nums.length; i++) {
//            if (i == ptr) continue;

        }
    }
}
