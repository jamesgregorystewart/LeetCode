import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Trie {

    class TrieNode {
        boolean isWord = false;
        String val;
        Map<String, TrieNode> characters = new HashMap<>();
    }

    public List<List<String>> wordSquares(String[] words) {

        TrieNode root = createTrie(words);
        List<List<String>> wordSquares = new ArrayList<>();

        for (int i = 0; i < words.length; i++) {

        }


        return wordSquares;

    }

    public TrieNode createTrie(String[] words) {
        TrieNode root = new TrieNode();

        TrieNode cur = root;
        for (String word : words) {
            for (char letter : word.toCharArray()) {
                if (cur.characters.keySet().contains(String.valueOf(letter))) {
                    cur = cur.characters.get(String.valueOf(letter));
                } else {
                    TrieNode newChar = new TrieNode();
                    newChar.val = String.valueOf(letter);
                    cur.characters.put(newChar.val, newChar);
                    cur = newChar;
                }
            }
            cur.isWord = true;
            cur = root;
        }
        return root;
    }
}