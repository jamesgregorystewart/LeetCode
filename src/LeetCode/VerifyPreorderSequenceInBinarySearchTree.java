package LeetCode;

public class VerifyPreorderSequenceInBinarySearchTree {

    /*
    * Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

    You may assume each number in the sequence is unique.

    Consider the following binary search tree:

         5
        / \
       2   6
      / \
     1   3
    Example 1:

    Input: [5,2,6,1,3]
    Output: false
    Example 2:

    Input: [5,2,1,3,6]
    Output: true
    Follow up:
    Could you do it using only constant space complexity?
    * */

    /*
    * once a number greater than root is seen then all numbers following must be greater than root
    * */

    public boolean verifyPreorder(int[] preorder) {
        return false;
    }
}