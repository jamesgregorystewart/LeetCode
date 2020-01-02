package Utility;

import java.util.LinkedList;

public class BinaryTreeTraverser {

    /*
    * This method will traverse a binary tree in level-order and print out the values of the nodes
    * */
    public String levelOrderTraverse(TreeNode tree) {

        StringBuilder str = new StringBuilder();

        LinkedList<TreeNode> nodes = new LinkedList<>();
        nodes.add(tree);
        while (!nodes.isEmpty()) {
            int N = nodes.size();
            for (int i = 0; i < N; i++) {
                TreeNode curr = nodes.poll();
                if (curr == null)
                    str.append("null,");
                else {
                    str.append(curr.val).append(",");
                    nodes.add(curr.left);
                    nodes.add(curr.right);
                }
            }
        }
        return str.toString();
    }
}
