package Chapter9;

import java.util.*;

public class Problem9_7 {

    class TreeNode {
        TreeNode left;
        TreeNode right;
    }

    public static void main(String args []) {
        Problem9_7 solution = new Problem9_7();
    }

    public List<TreeNode> inOrderTraversal(TreeNode node) {
        List<TreeNode> inorderList = new ArrayList<>();
        if (node == null) return inorderList;
        Stack<TreeNode> stack = new Stack<>();
        HashSet<TreeNode> visited = new HashSet<>();
        stack.push(node);

        do {
            if (node.left == null && node.right == null) { // we are at a leaf
                inorderList.add(node);
                visited.add(node);
                node = stack.pop();
            } else if (node.left != null && node.right != null && !visited.contains(node.left) && !visited.contains(node.right)) {
                stack.push(node.right);
                stack.push(node);
                node = node.left;
            } else if (node.left == null && node.right != null && !visited.contains(node.right)) {
                stack.push(node);
                node = node.right;
            } else if (node.left != null && node.right == null && !visited.contains(node.left)) {
                stack.push(node);
                node = node.left;
            }
        } while (!stack.isEmpty());

        return inorderList;
    }
}
