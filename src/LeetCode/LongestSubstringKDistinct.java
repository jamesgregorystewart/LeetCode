package LeetCode;

import java.util.*;

public class LongestSubstringKDistinct {

    public static void main(String[] args) {
        LongestSubstringKDistinct solution = new LongestSubstringKDistinct();
        System.out.println(solution.lengthOfLongestSubstringKDistinct("eceba", 2));
    }

    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (k == 0 || s.length() == 0) return 0;

        int max = 1;
        Set<Character> set = new HashSet<>();
        Map<Character, Integer> map = new HashMap<>();
        int left = 0; int right = 1;
        map.put(s.charAt(0), 1);
        set.add(s.charAt(0));

        int count = 1;
        while (right < s.length()) {
            char c = s.charAt(right++);
            map.put(c, map.getOrDefault(c, 0) + 1);
            set.add(c);
            count++;
            while (map.size() > k) {
                count--;
                char e = s.charAt(left++);
                map.put(e, map.get(e) - 1);
                if (map.get(e) == 0) {
                    map.remove(e);
                    set.remove(e);
                }
            }
            max = Math.max(max, count);
        }

        return max;
    }

}
