package Utility;

import java.util.HashMap;
import java.util.List;

public class Trie {

    class TrieNode {
        HashMap<Character, TrieNode> children;
        String str;
        boolean isWord;

        TrieNode(String str) {
            children = new HashMap<>();
            this.str = str;
            isWord = false;
        }
    }

    public TrieNode root;

    /* Initialize the Trie here */
    public Trie() {
        this.root = new TrieNode("");
    }

    public void build(List<String> dictionary) {
        for (String word : dictionary) {
            TrieNode curr = root;
            for (char c : word.toCharArray()) {
                if (curr.children.containsKey(c)) {
                    curr = curr.children.get(c);
                } else {
                    curr.children.put(c, new TrieNode(curr.str + c));
                    curr = curr.children.get(c);
                }
            }
        }
    }

    public void insert(String word) {
        TrieNode curr = root;
        for (char c : word.toCharArray()) {
            if (curr.children.containsKey(c)) {
                curr = curr.children.get(c);
            } else {
                curr.children.put(c, new TrieNode(curr.str + c));
                curr = curr.children.get(c);
            }
        }
    }

    public boolean isPrefix(String str) {
        TrieNode curr = root;
        for (char c : str.toCharArray()) {
            if (curr.children.containsKey(c)) {
                curr = curr.children.get(c);
            } else return false;
        }
        return true;
    }

    public boolean isWord(String str) {
        TrieNode curr = root;
        for (char c : str.toCharArray()) {
            if (curr.children.containsKey(c))
                curr = curr.children.get(c);
            else
                return false;
        }
        return curr.isWord;
    }
}
