package LeetCode;

public class BasicCalculatorII {

    public static void main(String[] args) {
        BasicCalculatorII solution = new BasicCalculatorII();
        System.out.println(solution.calculate("2/3+1*9"));
    }

    /*
    * Idea: Iteratively calculate the solution left -> right using PEMDAS
    * So: iterate from left to right 5 times looking for each of the above in order
    * */

    public int calculate(String s) {
        if (s.length() == 0) return 0;
        s = s.trim();

        // Multiplication
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '*')
                s = calc(s, i);
        }
        s = s.trim();
        // Division
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '/')
                s = calc(s, i);
        }
        s = s.trim();
        // Addition
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '+')
                s = calc(s, i);
        }
        s = s.trim();
        // Subtraction
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '-')
                s = calc(s, i);
        }
        s = s.trim();

        return Integer.valueOf(s);
    }

    private String calc(String s, int i) {
        int firstIdx = i - 1;
        int secondIdx = i + 1;
        while (s.charAt(firstIdx) >= 30 && s.charAt(firstIdx) <= 39) firstIdx--;
        while (s.charAt(secondIdx) >= 30 && s.charAt(secondIdx) <= 39) secondIdx++;
        int first = Integer.parseInt(s.substring(firstIdx, i));
        int second = Integer.parseInt(s.substring(i+1, secondIdx+1));
        Character operator = s.charAt(i);

        if (operator == '*')
            return s.substring(0, firstIdx) + (first * second) + s.substring(secondIdx+1);
        else if (operator == '/')
            return s.substring(0, firstIdx) + (first / second) + s.substring(secondIdx+1);
        else if (operator == '+')
            return s.substring(0, firstIdx) + (first + second) + s.substring(secondIdx+1);
        else
            return s.substring(0, firstIdx) + (first - second) + s.substring(secondIdx+1);
    }
}
