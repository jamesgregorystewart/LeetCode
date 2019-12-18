package LeetCode;

import java.util.HashSet;
import java.util.Set;

public class HappyNumber {

    public static void main(String[] args) {
        HappyNumber solution = new HappyNumber();
        System.out.println(solution.isHappy(81));
    }

    public boolean isHappy(int n) {
        if (n <= 0) return false;

        long calc = n;
        long sum;
        Set<Long> seen = new HashSet<>();

        while (calc != 1 && !seen.contains(calc)) {
            sum = 0;
            seen.add(calc);
            while (calc > 0) {
                long temp = calc%10;
                calc = calc/10;
                sum += temp*temp;
            }
            calc = sum;
        }
        return calc == 1;
    }
}
