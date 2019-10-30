package LeetCode;

import java.awt.*;
import java.util.*;
import java.util.List;

public class GroupAnagrams {

    public static void main(String[] args) {
        GroupAnagrams solution = new GroupAnagrams();
        System.out.println(solution.groupAnagrams(new String[] {"eat","tea","tan","ate","nat","bat"}));
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        List<List<String>> result = new ArrayList<>();

        for (String s : strs) {
            char[] char_sorted = s.toCharArray();
            Arrays.sort(char_sorted);
            String sorted = String.valueOf(char_sorted);
            map.putIfAbsent(sorted, new ArrayList<>());
            map.get(sorted).add(s);
        }
        for (Map.Entry<String, List<String>> entry : map.entrySet())
            result.add(entry.getValue());

        return result;
    }
}
