package LeetCode;
import java.util.Stack;

public class KthLargestElementInStream {

    public static void main(String[] args) {
        KthLargestElementInStream solution = new KthLargestElementInStream(2, new int[] {4,5,8,2});
        System.out.println(solution.add(3));
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
            TreeNode head = new TreeNode(nums[0]);
            kthLargest = head;
            treeSize++;

            for (int i = 1; i < nums.length; i++) addNode(nums[i]);
        }
    }

    /*

    Optimizations:
    - Sort the array that is provided and create a balanced BST in the constructor for the class
    - Balance the BST routinely to increase the time to perform operations

    * Step 1) add the new node to the tree DONE
    * Step 2) return kthLargest
    *   -> if the size of the tree is less than or equal to k then return kthlargest (it will be smallest node) DONE
    *   -> if the new val is larger than kthLargest, then recalculate kthLargest and return that
    *   -> else return kthLargest DONE
    * */
    public int add(int val) {
        if (head == null) {
            head = new TreeNode(val);
            return val; //TODO: check what the behavior should be like for these cases
        }
        // 1) Add node
        addNode(val);

        // 2) return kth largest
        if (treeSize <= k) return kthLargest.val; //TODO: need to check the behavior for these cases
        //need to reset the kthLargest
        if (val > kthLargest.val) setKthLargest();

        return kthLargest.val;
    }

    public void addNode(int val) {
        TreeNode toInsert = new TreeNode(val);
        TreeNode curr = head;
        TreeNode prev = curr;
        treeSize++;

        //find the spot to insert the new node
        while (curr != null) {
            prev = curr;
            curr = toInsert.val < curr.val ? curr.left : curr.right;
        }

        //insert the new node
        if (toInsert.val < prev.val) prev.left = toInsert;
        else prev.right = toInsert;
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
