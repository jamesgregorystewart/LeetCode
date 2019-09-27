package Chapter6;

public class Problem2 {

    public static String intToString(int x) {
        boolean isNegative = false;
        if (x < 0) isNegative = true;

        StringBuilder s = new StringBuilder();
        do {
            s.append((char)('0' + Math.abs(x % 10)));
            x/=10;
        } while (x != 0);

        return s.append(isNegative ? "-" : "").reverse().toString();
    }

    public static int stringToInt(String s) {
        return (s.charAt(0) == '-' ? -1 : 1) *
                s.substring(s.charAt(0) == '-' ? 1 : 0)
                .chars()
                .reduce(0, (runningSum, c) -> runningSum * 10 + c - '0');
    }
}
