package LeetCode;

public class LongestValidParentheses {


    public static void main(String[] args) {
        LongestValidParentheses solution = new LongestValidParentheses();
        System.out.println(solution.longestValidParentheses("((()()(()((()"));
        // ()()(()
        //((()()(()((()
    }
        /*
    * Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    Example 1:

    Input: "(()"
    Output: 2
    Explanation: The longest valid parentheses substring is "()"
    Example 2:

    Input: ")()())"
    Output: 4
    Explanation: The longest valid parentheses substring is "()()"
    * */

    /*
    * Idea: iterate from  left to right and whenever opening == closing -> set max
    * */

    private int max = 0;
    private int start = 0;

    public int longestValidParentheses(String s) {
        if (s == null || s.length() == 0) return 0;
        while (start < s.length()-1 && s.length() - start > max) {
            helper(s, start++);
        }
        return max;
    }

    private void helper(String s, int idx) {
        int opening = 0, closing = 0, running = 0;
        for (char c : s.substring(idx).toCharArray()) {
            running++;
            if (c == '(') opening++;
            else closing++;
            if (opening == closing) {
                max = Math.max(running, max);
            } else if (closing > opening) {
                start = idx + closing + opening;
                return;
            }
        }
    }
}
