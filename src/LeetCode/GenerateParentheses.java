package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class GenerateParentheses {

    public static void main(String[] args) {
        GenerateParentheses solution = new GenerateParentheses();
        System.out.println(solution.generateParenthesis(3));
    }

    /*
    * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"
    ]
    * */

    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        backtrack(result, "", n, 0, 0);
        return result;
    }

    public void backtrack(List<String> result, String str, int n, int open, int closed) {
        if (str.length() == n*2)
            result.add(str);
        else {
            if (open < n)
                backtrack(result, str + "(", n, open+1, closed);
            if (closed < open)
                backtrack(result, str + ")", n, open, closed+1);
        }
    }
}
