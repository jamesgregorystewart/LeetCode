package LeetCode;

import java.util.HashMap;
import java.util.Map;

public class MapSumPairs {

    class TrieNode {
        HashMap<Character, TrieNode> children;
        String str;
        boolean isWord;
        int sum;

        TrieNode(String str) {
            this.children = new HashMap<>();
            this.str = str;
            this.isWord = false;
            this.sum = 0;
        }
    }

    TrieNode root;


    /** Initialize your data structure here. */
    public MapSumPairs() {
        this.root = new TrieNode("");
    }

    public void insert(String key, int val) {
        TrieNode curr = root;
        for (char c : key.toCharArray()) {
            if (!curr.children.containsKey(c)) curr.children.put(c, new TrieNode(curr.str + c));
            curr = curr.children.get(c);
        }
        curr.isWord = true;
        curr.sum = val;
    }

    public int sum(String prefix) {
        TrieNode curr = root;

        for (char c : prefix.toCharArray()) {
            if (!curr.children.containsKey(c)) return 0; // prefix does not exist
            curr = curr.children.get(c);
        }

        return dfs(curr);
    }

    public int dfs(TrieNode node) {
        int runningSum = 0;
        for (Map.Entry<Character, TrieNode> entry: node.children.entrySet()) {
            runningSum += dfs(entry.getValue());
        }
        return node.sum + runningSum;
    }
}
