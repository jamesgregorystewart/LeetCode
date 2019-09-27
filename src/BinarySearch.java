public class BinarySearch {

    public boolean binarySearch(int[] nums, int target) {

        return helper(nums, target, 0, nums.length-1);
    }

    private boolean helper(int[] nums, int target, int front, int back) {
        int mid = (front + back) / 2;
        if (back <= front) return false;
        if (target == nums[mid]) return true;
        else if (target < nums[mid]) return helper(nums, target, front, mid - 1);
        else if (target > nums[mid]) return helper(nums, target, mid + 1, back);
        return false;
    }
}
