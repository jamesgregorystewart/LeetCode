package LeetCode;

import java.util.*;

public class WordSearchII {

    public static void main(String[] args) {
        HashSet<String> dug;
        WordSearchII solution = new WordSearchII();
        List<String> result = solution.findWords(new char[][] {{'o','a','a','n'},{'e','t','a','e'},{'i','h','k','r'},{'i','f','l','v'}}, new String[] {"oath", "pea", "eat", "rain"});
        for (String str : result) System.out.println(str);
    }

    TrieNode trie;

    //O(N) All elements in matrix
    public List<String> findWords(char[][] board, String[] words) {
        if (words.length == 0) return new ArrayList<>();
        HashSet<String> result = new HashSet<>();
        trie = new TrieNode("");
        buildTrie(words);
        for (int i = 0; i < board.length; ++i) { //the y coord
            for (int j = 0; j < board[0].length; ++j) { //the x coord
                if (trie.children.containsKey(board[i][j])) {
                    HashSet<Coordinate> visited = new HashSet<>();
                    Coordinate coord = new Coordinate(j, i);
                    TrieNode node = trie.children.get(board[coord.y][coord.x]);
                    visited.add(coord);
                    Stack<TrieNode> path = new Stack<>();
                    path.push(node);
                    dfs(board, result, coord, visited, node, path);
                }
            }
        }
        return new ArrayList<>(result);
    }

    //O(w*l)
    public void dfs(char[][] board, HashSet<String> result, Coordinate coord, HashSet<Coordinate> visited, TrieNode node,
                    Stack<TrieNode> path) {
        if (node.isWord) { //check if visited so we don't re-add while backtracking
            result.add(node.prefix);
            if (node.children.keySet().size() == 0) return;
        }
        List<Coordinate> list = new ArrayList<>();
        list.add(new Coordinate(coord.x-1, coord.y));
        list.add(new Coordinate(coord.x, coord.y+1));
        list.add(new Coordinate(coord.x, coord.y-1));
        list.add(new Coordinate(coord.x+1, coord.y));
        // dfs
        for (Coordinate next : list) {
            if (next.x >= 0 && next.x < board[0].length && next.y >= 0 && next.y < board.length && !visited.contains(next)
                    && node.children.containsKey(board[next.y][next.x])) {
                visited.add(next);
                path.push(node);
                node = node.children.get(board[next.y][next.x]);
                dfs(board, result, next, visited, node, path);
                visited.remove(next);
                node = path.pop();
            }
        }
    }

    public void buildTrie(String[] words) {
        for (String word : words) {
            TrieNode node = trie;
            for (char c : word.toCharArray()) {
                if (!node.children.containsKey(c)) node.children.put(c, new TrieNode(node.prefix+c));
                node = node.children.get(c);
            }
            node.isWord = true;
        }
    }

    class Coordinate {
        Integer x;
        Integer y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int hashCode() {
            return Integer.hashCode(x) ^ Integer.hashCode(y);
        }

        @Override
        public boolean equals(Object o) {
            if (o == null) return false;
            if (o == this) return true;
            Coordinate that = (Coordinate) o;
            return this.x == that.x && this.y == that.y;
        }
    }

    class TrieNode {
        HashMap<Character, TrieNode> children;
        String prefix;
        boolean isWord;

        public TrieNode(String str) {
            this.children = new HashMap<>();
            this.prefix = str;
            this.isWord = false;
        }
    }
}
