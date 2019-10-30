package LeetCode;
import java.util.Stack;

public class KthLargestElementInStream {

    public static void main(String[] args) {
        KthLargestElementInStream solution = new KthLargestElementInStream(2, new int[] {4,5,8,2});
        System.out.println(solution.add(3));
        System.out.println(solution.add(5));
    }

    class TreeNode {
        TreeNode left;
        TreeNode right;
        int val;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    TreeNode head = null;
    TreeNode kthLargest = null;
    int k;
    int treeSize = 0;

    //just builds the tree and does not jointly calculate the first kthlargest
    public KthLargestElementInStream(int k, int[] nums) {
        this.k = k;
        if (nums.length > 0) {
            for (int num : nums) addNode(num);
            setKthLargest();
        }
    }

    public int add(int val) {
        // 1) Add node
        addNode(val);

        // 2) return kth largest
        if (treeSize <= k) return kthLargest.val; //TODO: need to check the behavior for these cases
        //need to reset the kthLargest if there is a new largest
        if (val > kthLargest.val) setKthLargest();

        return kthLargest.val;
    }

    public void addNode(int val) {
        treeSize++;
        if (head == null) {
            this.head = new TreeNode(val);
            return;
        }

        TreeNode toInsert = new TreeNode(val);
        TreeNode curr = head;
        TreeNode prev = curr;

        //find the spot to insert the new node
        while (curr != null) {
            prev = curr;
            curr = toInsert.val < curr.val ? curr.left : curr.right;
        }

        if (toInsert.val < prev.val) prev.left = toInsert;
        else prev.right = toInsert;
//        if (prev != head) {
//
//        }
    }

    public void setKthLargest() {
        TreeNode curr = head;
        Stack<TreeNode> stack = new Stack<>();
        int countFromLargest = 0;

        // first: go to the rightmost (largest) and build stack of parents
        while (curr.right != null) {
            stack.push(curr);
            curr = curr.right;
        }

        // inorder predecessor will be the right most leaf of the left subtree -> or parent if that does not exist
        while (countFromLargest != k && curr != null) {
            if (curr.left != null) {
                curr = curr.left;
                while (curr.right != null) {
                    stack.push(curr);
                    curr = curr.right;
                }
            } else if (!stack.isEmpty()) {
                curr = stack.pop();
            }
            countFromLargest++;
        }
        kthLargest = curr;
    }
}
