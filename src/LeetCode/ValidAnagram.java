package LeetCode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class ValidAnagram {

    public static void main(String[] args) {
        ValidAnagram solution = new ValidAnagram();
        System.out.println(solution.isAnagram("", ""));
    }

    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        char [] s_chars = s.toCharArray();
        Arrays.sort(s_chars);
        char[] t_chars = t.toCharArray();
        Arrays.sort(t_chars);
        return String.valueOf(s_chars).equals(String.valueOf(t_chars));
    }
}

