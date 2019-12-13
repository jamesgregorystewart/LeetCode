package LeetCode;

import java.util.*;

public class BinaryTreeZigZagLevelOrderTraverse {

    /*
    * Idea:
    * - Level order traversal and reverse every odd indexed list in the result
    * */

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) return new ArrayList<>();
        List<List<Integer>> result = new ArrayList<>();

        Queue<TreeNode> q = new ArrayDeque<>();
        q.offer(root);
        while (!q.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            //iterate through the level
            int len = q.size();
            for (int i = 0; i < len; i++) {
                TreeNode curr = q.poll();
                level.add(curr.val);
                if (curr.left != null) q.add(curr.left);
                if (curr.right != null) q.add(curr.right);
            }
            result.add(level);
        }

        //create the zig-zag ordering within the collection
        for (int i = 1; i < result.size(); i+= 2) {
            Collections.reverse(result.get(i));
        }

        return result;
    }


    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            this.val = x;
        }
     }
}
