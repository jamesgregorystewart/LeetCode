package LeetCode;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public class LongestSubstringAtMostTwoChars {

    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (null == s) return 0;
        if (s.length() <= 2) return s.length();

        ArrayDeque<Character> window = new ArrayDeque<>();
        Set<Character> composition = new HashSet<>();
        int sPointer = 0;
        int removeIndex = 0;
        int max = 0;

        while (sPointer < s.length()) {
            if (composition.size() < 2) {
                composition.add(s.charAt(sPointer));
                if (((Character)s.charAt(sPointer)).compareTo(window.peekLast()) == 1) removeIndex = window.size();
                window.add(s.charAt(sPointer));
                sPointer++;
                max++;
            } else if (!composition.contains(s.charAt(sPointer))) {
                max = Math.max(window.size(), max);
                Character temp = window.peekLast();
                composition.clear();
                composition.add(temp);
                composition.add(s.charAt(sPointer));
                while (removeIndex > 0) {
                    window.removeFirst();
                    removeIndex--;
                }
                removeIndex = window.size();
                window.addLast(s.charAt(sPointer++));
            } else {
                if (((Character)s.charAt(sPointer)).compareTo(window.peekLast()) == 1) removeIndex = window.size();
                window.addLast(s.charAt(sPointer++));
                max = Math.max(max, window.size());
            }
            max = Math.max(max, window.size());
        }
        return max;
    }
}
