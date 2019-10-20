package LeetCode;


public class InorderSuccessor {

    public static void main(String[] args) {
        TreeNode root = new TreeNode(2);
        TreeNode left = new TreeNode(1);
        TreeNode right = new TreeNode(3);

        root.left = left;
        root.right = right;

        InorderSuccessor solution = new InorderSuccessor();
        TreeNode result = solution.inorderSuccessor(root, left);
        System.out.println(result.val);
    }

    TreeNode successor = null;
    boolean tagSuccessor = false;

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) return root;
        findSuccessor(root, p);
        return successor;
    }

    public void findSuccessor(TreeNode root, TreeNode target) {
        if (root == null || successor != null) return;

        findSuccessor(root.left, target);
        if (tagSuccessor) this.successor = root;
        if (root == target) this.tagSuccessor = true;
        findSuccessor(root.right, target);
    }

    static class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;

        TreeNode(int val) {
            this.val = val;
        }
    }
}
