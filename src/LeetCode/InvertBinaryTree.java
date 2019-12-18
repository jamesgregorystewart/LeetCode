package LeetCode;

public class InvertBinaryTree {

    /*
    * Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
    * */

    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        helper(root);
        return root;
    }

    public void helper(TreeNode root) {
        if (root == null) return;
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        helper(root.left);
        helper(root.right);
    }


    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }
}
