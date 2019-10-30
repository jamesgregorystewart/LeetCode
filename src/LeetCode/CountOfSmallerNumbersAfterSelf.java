package LeetCode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class CountOfSmallerNumbersAfterSelf {

    public static void main(String[] args) {
        CountOfSmallerNumbersAfterSelf solution = new CountOfSmallerNumbersAfterSelf();
        List<Integer> result;
        result = solution.countSmaller(new int[] {5,2,6,1});
        for (int num : result) System.out.println(num);
    }

    public List<Integer> countSmaller(int[] nums) {
        List<Integer> result = new ArrayList<>();
        TreeNode root = null;

        for (int i = nums.length - 1; i >= 0; i--) {
            if (root == null) {
                root = new TreeNode(nums[i]);
                result.add(0,0);
                continue;
            }
            TreeNode node = root;
            int count = 0;
            while (true) {
                if (node.val == nums[i]) {
                    node.count++;
                    break;
                }
                else if (node.left != null && nums[i] < node.val) node = node.left;
                else if (node.right != null && nums[i] > node.val){
                    count += node.count;
                    node = node.right;
                }
                else if (nums[i] < node.val) {
                    node.left = new TreeNode(nums[i]);
                    break;
                }
                else {
                    count += 1;
                    node.right = new TreeNode(nums[i]);
                    break;
                }
            }
            result.add(0, count);
        }
        return result;
    }

    class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;
        int count;

        public TreeNode (int val) {
            this.val = val;
            this.count = 1;
        }
    }
}
