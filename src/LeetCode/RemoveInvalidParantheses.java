package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class RemoveInvalidParantheses {

    /*
    * Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

    Note: The input string may contain letters other than the parentheses ( and ).

    Example 1:

    Input: "()())()"
    Output: ["()()()", "(())()"]
    Example 2:

    Input: "(a)())()"
    Output: ["(a)()()", "(a())()"]
    Example 3:

    Input: ")("
    Output: [""]
    *
    *
    * Thoughts:
    * - min amount to be removed will be the difference between openning and closing parens
    * - Need to identify the index range wherein we can perform paren operations
    * - Will remove all combinations of parens within the identified range of the paren type of which there are more
    *
    * Honestly... just recursively try removing every paren and add limitations afterwards
    * */

    public List<String> removeInvalidParentheses(String s) {
        if (s == null || s.length() <= 1) return new ArrayList<>();
        List<String> result = new ArrayList<>();



        return result;
    }
}
