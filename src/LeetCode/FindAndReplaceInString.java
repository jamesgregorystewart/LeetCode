package LeetCode;

import java.util.*;

public class FindAndReplaceInString {

    public static void main(String[] args) {
        FindAndReplaceInString solution = new FindAndReplaceInString();
        System.out.println(solution.findReplaceString("", new int[] {}, new String[] {}, new String[] {}));
    }

    public String findReplaceString(String S, int[] indexes, String[] sources, String[] targets) {
        StringBuilder ans = new StringBuilder();
        int[] match = new int[S.length()];
        Arrays.fill(match, -1);

        //build the array of matches
        for (int i = 0; i < indexes.length; i++) {
            int ix = indexes[i];
            if (S.substring(ix, ix+sources[i].length()).equals(sources[i]))
                match[ix] = i;
        }

        for (int i = 0; i < S.length(); i++) {
            if (match[i] >= 0) {
                ans.append(targets[match[i]]);
                i+= sources[match[i]].length() - 1;
            }
            else
                ans.append(S.charAt(i));
        }
        return ans.toString();
    }
}
