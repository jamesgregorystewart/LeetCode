package LeetCode;

public class RotatedSortedArray {

    public static void main(String[] args) {
        RotatedSortedArray solution = new RotatedSortedArray();
        System.out.println(solution.search(new int[] {4,5,6,7,0,1,2}, 7));
    }

    public int search(int[] nums, int target) {
        if (nums.length == 0) return -1;
        int left = 0;
        int pivot = 0;
        int right = nums.length-1;
        pivot = findPivot(nums, left, right);

        if (target >= nums[0] && target <= nums[pivot - 1])
            return findTarget(nums, 0, pivot-1, target);
        else if (target <= nums[nums.length-1] && target >= nums[pivot])
            return findTarget(nums, pivot, nums.length-1, target);
        else return -1;
    }

    public int findPivot(int[] nums, int front, int back) {
        int mid = front + (back - front) / 2;
        // if (mid -1 < 0 || mid + 1 > nums.length) return mid;
        if (nums[mid-1] > nums[mid]) return mid;
        if (nums[mid+1] < nums[mid]) return mid + 1;
        if (mid < front || mid < back) return findPivot(nums, front, mid-1);
        else return findPivot(nums, mid + 1, back);
    }

    public int findTarget(int[] nums, int front, int back, int target) {
        int mid = front + (back - front) / 2;
        // if (mid < front || mid > back) return -1;
        if (target == nums[mid]) return mid;
        else if (target > nums[mid]) return findTarget(nums, mid + 1, back, target);
        else return findTarget(nums, front, mid -1, target);
    }
}
