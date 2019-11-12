package LeetCode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ParitionLabels {

    public List<Integer> partitionLabels(String S) {
        List<Integer> result = new ArrayList<>();
        if (S.length() == 0) return result;

        Map<Character, Integer> map = new HashMap();
        //iterate through first and create the map
        for (int i = 0; i < S.length(); i++) {
            map.put(S.charAt(i), i);
        }

        int max = map.get(S.charAt(0));
        int count = 0;
        for (int i = 0; i < S.length(); i++) {
            count++;
            max = Math.max(max, map.get(S.charAt(i)));
            if (max == i) {
                result.add(count);
                count = 0;
            }
        }
        return result;
    }
}
