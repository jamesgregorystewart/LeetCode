package Utility;

public class TreeNode {

    public TreeNode left;
    public TreeNode right;
    public int val;

    public TreeNode(int val) {
        this.val = val;
    }

    public TreeNode(String val) {
        this.val = Integer.getInteger(val);
    }
}
