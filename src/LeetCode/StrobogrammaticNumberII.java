package LeetCode;

import java.util.ArrayList;
import java.util.List;

public class StrobogrammaticNumberII {

    public static void main(String[] args) {
        StrobogrammaticNumberII solution = new StrobogrammaticNumberII();
        List<String> result = solution.findStrobogrammatic(3);
        for (String str : result)
            System.out.println(str);
    }

    char[] chars = new char[] {'0','1', '8', '6', '9'};

    public List<String> findStrobogrammatic(int n) {
        if (n < 0) return new ArrayList<>();

        List<String> result = new ArrayList<>();
        backtrack(result, new char[n], 0, n-1);
        return result;
    }

    public void backtrack(List<String> result, char[] tempList, int left, int right) {
        if (left > right) result.add(String.valueOf(tempList));
        else {
            for (char num : chars) {
                if (left == right) {
                    if (num == '6' || num == '9') return;
                    else tempList[left++] = num;
                    right--;
                }
                else if (num == '6') {
                    tempList[left++] = '6';
                    tempList[right--] = '9';
                } else if (num == '9') {
                    tempList[left++] = '9';
                    tempList[right--] = '6';
                } else {
                    if (left == 0 && num == '0') continue;
                    tempList[left++] = num;
                    tempList[right--] = num;
                }
                backtrack(result, tempList, left, right);
                --left;
                ++right;
            }
        }
    }
}
