package LeetCode;

public class ReverseWordsInString {

    public static void main(String[] args) {
        ReverseWordsInString solution = new ReverseWordsInString();
        System.out.println(solution.reverseWords("a good   example"));
    }

    public String reverseWords(String s) {
        s = s.trim();
        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();
        for (int i = words.length-1; i >0; i--) {
            if (!words[i].equals("")) result.append(words[i] + " ");
        }
        result.append(words[0]);
        return result.toString();
    }
}
