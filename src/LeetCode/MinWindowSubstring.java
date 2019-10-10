package LeetCode;

import java.util.HashMap;
import java.util.Map;

public class MinWindowSubstring {

    public static void main(String[] args) {
        MinWindowSubstring solution = new MinWindowSubstring();
        int[] counts = new int[128];
        counts['d']++;
        for (int count : counts)
            System.out.println(count);
//        System.out.println(solution.minWindow("ADOBECODEBANC", "ABC"));
    }

    public String minWindow(String s, String t) {
        String result = s;
        String build = "";
        if (s.length() < t.length() || s.length() == t.length() && !s.equals(t)) return "";
        int n = s.length();
        int m = t.length();
        int front = 0;
        int back = m;

        HashMap<Character, Integer> tMap = new HashMap<>();
        HashMap<Character, Integer> sMap = new HashMap<>();

        //load up the maps
        for (int i = 0; i < m; i ++) {
            if (tMap.putIfAbsent(t.charAt(i), 1) != null) //put if not there
                tMap.put(t.charAt(i), tMap.get(t.charAt(i)) + 1); // if there then increment the val

            if (sMap.putIfAbsent(s.charAt(i), 1) != null) //put if not there
                sMap.put(s.charAt(i), sMap.get(s.charAt(i)) + 1); // if there then increment the val
        }

        while (back < n || contains(tMap, sMap)) {
            if (contains(tMap, sMap)) {
                build = s.substring(front, back);
                if (build.length() < result.length())
                    result = build;
                sMap.put(s.charAt(front), sMap.get(s.charAt(front))-1);
                front++;
            } else {
                if (sMap.putIfAbsent(s.charAt(back), 1) != null) //put if not there
                    sMap.put(s.charAt(back), sMap.get(s.charAt(back)) + 1); // if there then increment the val
                back++;
            }
        }
        return build.length() < result.length() ? build : result;
    }

    private boolean contains(HashMap<Character, Integer> tMap, HashMap<Character, Integer> sMap) {
        for (Character key : tMap.keySet()) {
            if (!sMap.containsKey(key)) return false;
            if (sMap.get(key) < tMap.get(key)) return false;
        }
        return true;
    }
}
