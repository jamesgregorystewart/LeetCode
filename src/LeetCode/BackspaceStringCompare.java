package LeetCode;

public class BackspaceStringCompare {

    public static void main(String[] args) {
        BackspaceStringCompare solution = new BackspaceStringCompare();
        System.out.println(solution.backspaceCompare("ab##", "c#d#d"));
    }

    /*
    * O(N) time and O(1) space
    * */

    public boolean backspaceCompare(String S, String T) {

        int sPtr = 0;
        int tPtr = 0;
        while (sPtr < S.length() || tPtr < T.length()) {
            if (sPtr < S.length()) {
                if (S.charAt(sPtr) == '#') {
                    if (sPtr > 0 && sPtr < S.length() -1) S = S.substring(0, sPtr-1) + S.substring(sPtr--+1);
                    else if (sPtr == 0 && sPtr < S.length() -1) S = S.substring(sPtr+1);
                    else if (sPtr == 0) S = "";
                    else S = S.substring(0, sPtr-1);
                } else sPtr++;
            }

            if (tPtr < T.length()) {
                if (T.charAt(tPtr) == '#') {
                    if (tPtr > 0 && tPtr < T.length() -1) T = T.substring(0, tPtr-1) + T.substring(tPtr--+1);
                    else if (tPtr == 0 && tPtr < T.length() -1) T = T.substring(tPtr+1);
                    else if (tPtr == 0) T = "";
                    else T = T.substring(0, tPtr-1);
                } else tPtr++;
            }
        }
        return S.equals(T);
    }
}
