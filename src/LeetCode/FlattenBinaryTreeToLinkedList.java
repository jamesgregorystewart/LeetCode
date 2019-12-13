package LeetCode;

import java.util.Stack;

public class FlattenBinaryTreeToLinkedList {

    /*
    * Given a binary tree, flatten it to a linked list in-place.

    For example, given the following tree:

        1
       / \
      2   5
     / \   \
    3   4   6
    The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6
    * */

    /*
    * Idea:
    * - Need to set the right pointer of curr to what is returned from inOrder result
    * - Meanwhile you need to set the right pointer of the greatest child of inorder to the right of curr
    * */

    public void flatten(TreeNode root) {
        if (root == null) return;

        TreeNode curr = root;
        while (curr != null) {
            TreeNode left = curr.left;
            if (left == null) {
                curr = curr.right;
                continue;
            }
            TreeNode greatestLeft = left;
            while (greatestLeft.right != null) greatestLeft = greatestLeft.right;
            greatestLeft.right = curr.right; //if inOrder is the only child then inOrderGreatest == inOrder
            curr.right = left;
            curr.left = null;
            curr = curr.right;
        }
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }
}
