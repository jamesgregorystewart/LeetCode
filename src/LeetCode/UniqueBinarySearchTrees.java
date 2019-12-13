package LeetCode;

import java.util.HashSet;

public class UniqueBinarySearchTrees {

    public static void main(String[] args) {

    }

    /*
    *Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

    Example:

    Input: 3
    Output: 5
    Explanation:
    Given n = 3, there are a total of 5 unique BST's:

       1         3     3      2      1
        \       /     /      / \      \
         3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3


   Idea:
   - Simulation based approach -> build the trees and count how many you can make
   - There might be a math approach but I won't spend time on this

   Procedure:
   - Recursive backtracking building a tree and also deleting nodes from the tree as you backtrack
   - Encode the tree as a comma-separated string and put into a hashset
    * */

    int trees;

    //TODO: Did not finish this problem as the solutions were 1) Dynamic programming and 2) Mathematic deduction (i.e. not really a tree problem)
    public int numTrees(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        this.trees = 0;

        backtrack(n, 0, new StringBuilder(), new HashSet<>());
        return trees;
    }

    private void backtrack(int last, int curr, StringBuilder str, HashSet<String> seen) {
        if (curr == last && !seen.contains(str.toString())) {
            seen.add(str.toString());
            trees++;
        } else {

        }
    }
}
