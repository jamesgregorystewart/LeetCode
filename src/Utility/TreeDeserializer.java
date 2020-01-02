package Utility;

import com.sun.source.tree.Tree;

public class TreeDeserializer {

    private int childP = 3;

    public TreeNode deserialize(String[] tree) {
        if (tree == null || tree.length == 0) return null;

        TreeNode root = new TreeNode(tree[0]);
        root.left = deserializeHelper(tree, 1);
        root.right = deserializeHelper(tree, 2);

        return root;
    }

    private TreeNode deserializeHelper(String[] tree, int head) {
        if (head >= tree.length || tree[head] == null) return null;
        TreeNode root = new TreeNode(tree[head]);
        root.left = deserializeHelper(tree, childP++);
        root.right = deserializeHelper(tree, childP++);
        return root;
    }

}
