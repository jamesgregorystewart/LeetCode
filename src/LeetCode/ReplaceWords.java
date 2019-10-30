package LeetCode;

import java.util.HashMap;
import java.util.List;

public class ReplaceWords {

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

    public String replaceWords(List<String> dict, String sentence) {
        root = new TrieNode("");

        //1) Add all roots to Trie
        for (String word : dict) {
            TrieNode curr = root;

            for (char c : word.toCharArray()) {
                if (!curr.children.containsKey(c)) curr.children.put(c, new TrieNode(curr.str+c));
                curr = curr.children.get(c);
            }
            curr.isWord = true;
        }

        String[] words = sentence.split(" ");

        for (int i = 0; i < words.length; i++) {
            TrieNode curr = root;
            for (char c : words[i].toCharArray()) {
                if (curr.isWord) {
                    words[i] = curr.str;
                    break;
                }
                if (!curr.children.containsKey(c)) break;
                curr = curr.children.get(c);
            }
        }
        return String.join(" ", words);
    }
}
