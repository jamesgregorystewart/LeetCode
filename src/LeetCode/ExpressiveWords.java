package LeetCode;

public class ExpressiveWords {

    public static void main(String[] args) {
        ExpressiveWords solution = new ExpressiveWords();
        System.out.println(solution.expressiveWords("aaa", new String[] {"aaaa"}));
    }

    public int expressiveWords(String S, String[] words) {
        int ans = 0;

        for (int i = 0; i < words.length; i++) {
            int sP = 0;
            int wP = 0;
            while (wP < words[i].length() && sP < S.length()) {
                if (words[i].charAt(wP) != S.charAt(sP)) break; // words are different -> break

                int groupSize = 0;

                int temp_sP = sP;
                int temp_wP = wP;
                boolean firstPass = true;
                //count group size
                while(temp_wP < words[i].length() && temp_sP < S.length() && words[i].charAt(temp_wP) == S.charAt(temp_sP)) {
                    if (!firstPass && words[i].charAt(temp_wP) != words[i].charAt(temp_wP-1)) break;
                    groupSize++;
                    temp_sP++;
                    temp_wP++;
                    firstPass = false;
                }

                int stretch = 0;
                //move along the stretch
                while (sP < S.length()  && wP < words[i].length() && words[i].charAt(wP) == S.charAt(sP)) {
                    stretch++;
                    sP+=1;
                }
                if (stretch < 3 && stretch != groupSize) break;
                else
                    wP += groupSize;
            }
            if (wP == words[i].length() && !words[i].equals("") && sP == S.length()) ans++;
        }
        return ans;
    }
}
