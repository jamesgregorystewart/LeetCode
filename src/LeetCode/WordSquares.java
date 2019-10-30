package LeetCode;

/*
* 1) Build a trie from all of the words that we are using
* 2) Backtrack:
*       a) add words one by one from the list that we have available and check with the trie that it is valid by iterating down each col
* */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class WordSquares {

    public static void main(String[] args) {
        WordSquares solution = new WordSquares();
        List<List<String>> ans = solution.wordSquares(new String[] {"abaa","aaab","baaa","aaba"});
        for (List<String> wordSq : ans) {
            for (String word : wordSq) {
                System.out.println(word);
            }
            System.out.println("-----");
        }
    }

    TrieNode root;

    public List<List<String>> wordSquares(String[] words) {
        root = new TrieNode();
        List<List<String>> ans = new ArrayList<>();
        if (words.length == 0) return ans;

        buildTrie(words);

        for (String word : words) {
            List<String> tempList = new ArrayList<>();
            tempList.add(word);
            backtrack(words, tempList, ans, 1);
        }

        return ans;
    }

    //would need to change this to remove first for loop and instead pass an int with each backtrack call
    public void backtrack(String[] words, List<String> tempList, List<List<String>> result, int step) {
        //if the size of templist == words[0].length() && every column is also a word found in the trie then add templist to result
        if (step == words[0].length()) {
            result.add(new ArrayList<>(tempList));
            return;
        }
        StringBuilder prefix = new StringBuilder();
        for (String word : tempList) {
            prefix.append(word.charAt(step));
        }
        for (Integer wordIndex : getWordsWithPrefix(prefix.toString())) {
            tempList.add(words[wordIndex]);
            backtrack(words, tempList, result, step + 1);
            tempList.remove(tempList.size() - 1);
        }
    }

    // O(W*L) W == words;  L == word length
    public void buildTrie(String[] words) {
        for (int i = 0; i < words.length; i++) {
            TrieNode node = root;
            for (char c : words[i].toCharArray()) {
                if (!node.children.containsKey(c)) node.children.put(c, new TrieNode());
                node = node.children.get(c);
                node.wordList.add(i); // add the index of the word with the prefix into the wordlist of the node
            }
        }
    }

    public List<Integer> getWordsWithPrefix(String prefix) {
        TrieNode node = root;
        for (char c : prefix.toCharArray()) {
            if (!node.children.containsKey(c)) return new ArrayList<>(); //nothing found so return an empty list
            node = node.children.get(c);
        }
        return node.wordList;
    }

    class TrieNode {
        HashMap<Character, TrieNode> children;
        List<Integer> wordList;

        public TrieNode () {
            this.wordList = new ArrayList<>();
            this.children = new HashMap<>();
        }
    }
}
