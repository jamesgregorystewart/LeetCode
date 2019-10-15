package LeetCode;

public class ValidPerfectSquare {

    static public void main(String[] args) {
        ValidPerfectSquare solution = new ValidPerfectSquare();
        System.out.println(solution.isPerfectSquare(808201));
    }

    public boolean isPerfectSquare(int num) {
        if (num == 1) return true;

        int left = 2;
        int right = num / 2;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long sq = (long) mid * mid;
            if (sq == num) return true;
            else if (sq > num && (long)(mid - 1) * (mid - 1) < num) return false;
            else if (sq < num && (long)(mid + 1) * (mid + 1) > num) return false;
            else if (sq < num) left = mid + 1;
            else right = mid - 1;
        }
        return false;
    }
}
