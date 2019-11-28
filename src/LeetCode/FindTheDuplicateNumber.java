package LeetCode;

public class FindTheDuplicateNumber {

    public static void main(String[] args) {
        FindTheDuplicateNumber solution = new FindTheDuplicateNumber();
        System.out.println(solution.findDuplicate(new int[] {3,1,3,4,2}));
    }

    public int findDuplicate(int[] nums) {

        int tortoise = nums[0];
        int hare = nums[0];

        do {
            tortoise = nums[tortoise];
            hare = nums[nums[hare]];
        } while (tortoise != hare);

        int ptr1 = tortoise;
        int ptr2 = nums[0];
        while(ptr1 != ptr2) {
            ptr1 = nums[ptr1];
            ptr2 = nums[ptr2];
        }
        return ptr1;
    }
}
