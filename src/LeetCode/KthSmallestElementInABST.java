package LeetCode;

import com.sun.source.tree.Tree;

import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class KthSmallestElementInABST {


    /*
    * Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

    Note:
    You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

    Example 1:

    Input: root = [3,1,4,null,2], k = 1
       3
      / \
     1   4
      \
       2
    Output: 1
    Example 2:

    Input: root = [5,3,6,2,4,null,null,1], k = 3
           5
          / \
         3   6
        / \
       2   4
      /
     1
    Output: 3
    Follow up:
    What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
    *
    * // In order traversal from smallest iterating 'k' times
    *   WORST: O(N) with O(N) memory because we need a stack
    * */

    public int kthSmallest(TreeNode root, int k) {
        TreeNode smallest = root;

        Stack<TreeNode> stack = new Stack<>();
        while (smallest.left != null) {
            stack.push(smallest);
            smallest = smallest.left;
        }


        int iterations = k-1;
        //perform inorder traversal k-1 times
        while (iterations-- != 0) {
            smallest = nextInOrder(smallest, stack);
        }

        return smallest.val;
    }

    public TreeNode nextInOrder(TreeNode node, Stack<TreeNode> stack) {
        if (node.right != null) {
            node = node.right;
            while (node.left != null) {
                stack.push(node);
                node = node.left;
            }
        } else { //shouldn't need to worry about stack being empty here if k is less than N
            node = stack.pop();
        }
        return node;
    }

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
    }
}
