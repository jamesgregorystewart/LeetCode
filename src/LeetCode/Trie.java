package LeetCode;

import java.util.HashMap;

public class Trie {

    class TrieNode {
        HashMap<Character, TrieNode> children;
        String str;
        boolean isWord;

        TrieNode(String str) {
            this.str = str;
            this.children = new HashMap<>();
            this.isWord = false;
        }
    }

    TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        this.root = new TrieNode("");
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.str.equals(word)) return;
            if (!curr.children.containsKey(c)) {
                curr.children.put(c, new TrieNode(curr.str+c));
            }
            curr = curr.children.get(c);
        }
        curr.isWord = true;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (!curr.children.containsKey(c)) return false;
            curr = curr.children.get(c);
        }
        return curr.isWord;
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        TrieNode curr = root;
        for (char c : prefix.toCharArray()) {
            if (!curr.children.containsKey(c)) return false;
            curr = curr.children.get(c);
        }
        return true;
    }
}
