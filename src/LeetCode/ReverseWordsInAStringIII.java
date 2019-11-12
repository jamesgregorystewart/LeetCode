package LeetCode;

public class ReverseWordsInAStringIII {

    public static void main(String[] args) {
        ReverseWordsInAStringIII solution = new ReverseWordsInAStringIII();
        System.out.println(solution.reverseWords("Let's take LeetCode contest"));
    }

    public String reverseWords(String s) {
        s = s.trim();
        int curr = 0;
        StringBuilder result = new StringBuilder();
        while (curr < s.length()) {
            if (s.charAt(curr) == ' ') {
                result.append(" ");
                curr++;
            }
            else {
                StringBuilder word = new StringBuilder();
                while (curr < s.length() && s.charAt(curr) != ' ') {
                    word.append(s.charAt(curr));
                    curr++;
                }
                result.append(word.reverse().toString());
            }
        }
        return result.toString();
    }
}
