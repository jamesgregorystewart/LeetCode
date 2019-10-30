package LeetCode;

class FlipEquivalentBinaryTrees {

    public static void main(String[] args) {

    }

    boolean ans;

    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        ans = true;
        helper(root1, root2);
        return ans;
    }

    public void helper(TreeNode root1, TreeNode root2) {
        if (!ans || (root1 == null && root2 == null)) return;
        if (root1 == null || root2 == null) {
            ans = false;
            return;
        }
        //same number of children?
        int lc = 0, rc = 0;
        if (root1.left != null) lc++;
        if (root1.right != null) lc++;
        if (root2.left != null) rc++;
        if (root2.right != null) rc++;
        if (lc != rc) {
            ans = false;
            return;
        }
        //no children on either side
        if (lc == 0) return;

        TreeNode root2L = null;
        if (root1.left != null) {
            if (root2.left == null) root2L = root2.right;
            else root2L = root1.left.val == root2.left.val ? root2.left : root2.right;
        }

        TreeNode root2R = null;
        if (root1.right != null) {
            if (root2.right == null) root2R = root2.left;
            else root2L = root1.right.val == root2.right.val ? root2.right : root2.left;
        }

        helper(root1.left, root2L);
        helper(root1.right, root2R);
    }

    class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;

        public TreeNode(int val) {
            this.val = val;
        }
    }
}
