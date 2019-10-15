package LeetCode;

public class ClosestBinarySearchTreeValue {

    public static void main(String[] args) {

    }

    /*
    * if the value is greater than root go to right subtree
    * if the value is less than root for to left subtree
    *
    * */

    public int closestValue(TreeNode root, double target) {
        int closest = root.val;

        while (root != null) {
            if (target > root.val && root.right == null) break;
            if (target < root.val && root.left == null) break;
            if (target > root.val) root = root.right;
            else if (target < root.val) root = root.left;
            else break;
            if (Math.abs(target - root.val) < Math.abs(target - closest)) closest = root.val;
        }
        return closest;
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }
}
