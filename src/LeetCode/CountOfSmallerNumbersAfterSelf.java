package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class CountOfSmallerNumbersAfterSelf {

    public static void main(String[] args) {
        CountOfSmallerNumbersAfterSelf solution = new CountOfSmallerNumbersAfterSelf();
        List<Integer> result;
        result = solution.countSmaller(new int[] {26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41});
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
                    count += node.leftCount;
                    break;
                }
                else if (node.left != null && nums[i] < node.val) {
                    node.leftCount++;
                    node = node.left;
                }
                else if (node.right != null && nums[i] > node.val){
                    count += (node.count + node.leftCount);
                    node = node.right;
                }
                else if (nums[i] < node.val) {
                    node.leftCount++;
                    node.left = new TreeNode(nums[i]);
                    break;
                }
                else {
                    count += (node.count + node.leftCount);
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
        int leftCount;

        public TreeNode (int val) {
            this.val = val;
            this.count = 1;
            this.leftCount = 0;
        }
    }
}
