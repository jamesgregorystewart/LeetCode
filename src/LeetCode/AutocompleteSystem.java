package LeetCode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class AutocompleteSystem {

    TrieNode root;
    StringBuilder inputStr;
    List<String> inputResults;

    public AutocompleteSystem(String[] sentences, int[] times) {
        TrieNode root = new TrieNode("");
         inputStr = new StringBuilder();
        int N = sentences.length;
        inputResults = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            String sentence = sentences[i];
            TrieNode node = root;
//            while (node !=)
        }
    }

    public List<String> input(char c) {
        return new ArrayList<>();
    }

    class TrieNode {
        int count;
        Map<Character, TrieNode> map;
        String str;

        public TrieNode(String str) {
            count = 1;
            this.str = str;
            map = new HashMap<>();
        }
    }
}

/**
 * Your AutocompleteSystem object will be instantiated and called as such:
 * AutocompleteSystem obj = new AutocompleteSystem(sentences, times);
 * List<String> param_1 = obj.input(c);
 */
