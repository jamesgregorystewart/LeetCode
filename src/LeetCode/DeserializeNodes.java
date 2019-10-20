package LeetCode;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class DeserializeNodes {

    public static void main(String[] args) {
        DeserializeNodes solution = new DeserializeNodes();
        System.out.println(solution.deserialize("1,2,null,null,3,4,null,null,5,null,null,"));
    }

    public TreeNode deserialize(String data) {
        String[] vals = data.split(",");
        List<String> list = new LinkedList<>(Arrays.asList(vals));
        return deserializeHelper(list);
    }

    public TreeNode deserializeHelper(List<String> vals){
        if (vals.get(0).equals("null")) {
            vals.remove(0);
            return null;
        }
        int val = Integer.valueOf(vals.get(0));
        vals.remove(0);
        TreeNode root = new TreeNode(val);
        root.left = deserializeHelper(vals);
        root.right = deserializeHelper(vals);
        return root;
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
