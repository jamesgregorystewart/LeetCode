package LeetCode;

import java.util.HashSet;

public class StringTransformsIntoAnotherString {

    public static void main(String[] args) {
        StringTransformsIntoAnotherString solution = new StringTransformsIntoAnotherString();
        System.out.println(solution.canConvert("bcdefghijklmnopqrstuvwxyza", "abcdefghijklmnopqrstuvwxyz"));
    }

    /*
    * "abcdefghijklmnopqrstuvwxyz"
"bcdefghijklmnopqrstuvwxyzq"
    * */

    public boolean canConvert(String str1, String str2) {
        if (str1.equals(str2)) return true;
        HashSet<Character>[] mappings = new HashSet[26];
        HashSet<Character> str2Seen = new HashSet<>();
        int N = str1.length();
        int used1 = 0;
        int used2 = 0;

        for (int i = 0; i < N; i++) {
            char c = str1.charAt(i);
            int idx = c - 'a';
            if (str2Seen.add(str2.charAt(i))) used2++;
            if (mappings[idx] == null) {
                mappings[idx] = new HashSet<>();
                used1++;
            }
            mappings[idx].add(str2.charAt(i));
        }
        for (HashSet<Character> mapping : mappings) {
            if (mapping == null) continue;
            if (mapping.size() > 1) return false;
        }
        if (used1 < 26) return true;
        return used2 != 26;
    }
}
