package LeetCode;

public class AddBinary {

    public static void main(String[] args) {
        AddBinary sol = new AddBinary();
        System.out.println(sol.addBinary("1011", "1010"));
    }

    StringBuilder result = new StringBuilder();

    public String addBinary(String a, String b) {
        helper(a, b, a.length()-1, b.length()-1, '0');
        return result.reverse().toString();
    }

    public void helper(String a, String b, int a_idx, int b_idx, char carryover) {
        if (a_idx < 0 && b_idx < 0) {
            if (carryover == '1') result.append(carryover);
            return;
        }
        int ones = 0;
        if (a_idx >= 0 && a.charAt(a_idx) == '1') ones++;
        if (b_idx >= 0 && b.charAt(b_idx) == '1') ones++;
        if (carryover == '1') ones++;

        if (ones == 0) {
            result.append("0");
            helper(a, b, --a_idx, --b_idx, '0');
        } else if (ones == 1) {
            result.append("1");
            helper(a, b, --a_idx, --b_idx, '0');
        } else if (ones == 2) {
            result.append("0");
            helper(a, b, --a_idx, --b_idx, '1');
        } else if (ones == 3) {
            result.append("1");
            helper(a, b, --a_idx, --b_idx, '1');
        }
    }
}
