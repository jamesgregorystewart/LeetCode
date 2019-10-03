package Chapter9;

import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;

public class Problem9_6_Varient {

    public static class TreeNode {
        int weight;
        TreeNode left = null;
        TreeNode right = null;

        TreeNode(int weight) {
            this.weight = weight;
        }
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(0);
        TreeNode left = new TreeNode(3);
        TreeNode right = new TreeNode(5);
        root.left = left;
        root.right = right;

        Problem9_6_Varient solution = new Problem9_6_Varient();
        List<List<TreeNode>> result = solution.pathsToLeaves(root, 1);
        for (List<TreeNode> list: result)
            for (TreeNode node : list)
                System.out.println(node.weight);
    }

    public List<List<TreeNode>> pathsToLeaves(TreeNode node, int weight) {
        List<List<TreeNode>> result = new ArrayList<>();
        List<TreeNode> tempList = new ArrayList<>();
        backtrack(result, tempList, node, weight);
        return result;
    }

    public void backtrack(List<List<TreeNode>> result, List<TreeNode> tempList, TreeNode node, int remainingWeight) {
        if (node == null || node.right == null && node.left == null && remainingWeight != 0) return;
        else if (node.right == null && node.left == null && remainingWeight == 0) {
            tempList.add(node);
            result.add(new ArrayList<>(tempList));
        }
        else {
            tempList.add(node);
            if (node.left != null) backtrack(result, tempList, node.left, remainingWeight - node.left.weight);
            if (node.right != null) backtrack(result, tempList, node.right, remainingWeight - node.right.weight);
            tempList.remove(tempList.size() - 1);
        }
    }
}
