package LeetCode;

import java.util.HashSet;
import java.util.Set;

public class NextClosestTime {

    public static void main(String[] args) {
        NextClosestTime solution = new NextClosestTime();
        System.out.println(solution.nextClosestTime("01:34"));
    }

    public String nextClosestTime(String time) {
        int start = Integer.parseInt(time.substring(0,2))*60;
        start += Integer.parseInt(time.substring(3,5));
        int ans = start;
        int elapsed = 24*60;
        Set<Integer> allowed = new HashSet<>();
        for (char c : time.toCharArray()) if (c != ':') allowed.add(c-'0');

        for (int h1 : allowed) for (int h2 : allowed) if (h1*10 + h2 < 24) {
            for (int m1 : allowed) for (int m2 : allowed) if (m1*10 + m2 < 60) {
                int cur = 60 * (10 * h1 + h2) + (10 * m1 + m2);
                int candElapsed = Math.floorMod(cur - start, 24*60);
                if (0 < candElapsed && candElapsed < elapsed) {
                    ans = cur;
                    elapsed = candElapsed;
                }
            }
        }
        return String.format("%02d:%02d", ans/60, ans%60);
    }
}
