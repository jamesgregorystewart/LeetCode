package LeetCode;

public class SlidingWindowMax {

    public static void main(String[] args) {
        SlidingWindowMax solution = new SlidingWindowMax();
        int[] ans = solution.maxSlidingWindow(new int[] {1,3,-1,-3,5,3,6,7}, 3);
        for (int num : ans) System.out.println(num);
    }

    /*
    * Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

    Example:

    Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
    Output: [3,3,5,5,6,7]
    Explanation:

    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7
    Note:
    You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

    Follow up:
    Could you solve it in linear time?


    Idea:
    - slide a window across keeping track of the count
    - when a max is found replace the values in the return array with the new max window
    * */

    public int[] maxSlidingWindow(int[] nums, int k) {
        if (k == 0) return new int[] {}; //validate this

        int ptr = 1;
        long count = nums[0];
        long max = Integer.MIN_VALUE;
        int[] window = new int[k];
        while (ptr < k) count += nums[ptr++]; //this is right
        max = Math.max(max, count);

        //O(N)
        while (ptr < nums.length) { //this is right
            count += nums[ptr];
            count -= nums[ptr-k];
            if (count > max) {
                //replace window contents (may want to maintain the starting index of max and go back to fill array at that point)
                for (int i = 0; i < window.length; i++) {
                    window[i] = nums[(ptr-(k-1))+i];
                }
                max = count;
            }
            ptr++;
        }

        return window;
    }
}
