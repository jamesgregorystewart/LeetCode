package LeetCode;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class ReorderDataInLogFiles {

    /*
    * O(3Nlog(N)) -> O(Nlog(N))
    * */

    public static void main(String[] args) {
        ReorderDataInLogFiles solution = new ReorderDataInLogFiles();
        String[] ans = solution.reorderLogFiles(new String[] {"a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"});
        for (String log : ans) System.out.println(log);
    }

    // O(Nlog(N)
    public String[] reorderLogFiles(String[] logs) {
        PriorityQueue<String> q = new PriorityQueue<>(logs.length, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int subStringIndex1 = o1.indexOf(" ");
                int subStringIndex2 = o2.indexOf(" ");
                if (o1.substring(subStringIndex1+1).compareTo(o2.substring(subStringIndex2+1)) == 0) {
                    return o1.compareTo(o2);
                }
                else return o1.substring(subStringIndex1+1).compareTo(o2.substring(subStringIndex2+1));
            }
        });
        List<String> digits = new ArrayList<>();

        //O(N)
        for (String log : logs) {
            if (log.charAt(log.length()-1) < 'a') digits.add(log);
            else q.offer(log);
        }
        String[] result = new String[logs.length];
        int resultPointer = 0;

        //O(N)
        while (!q.isEmpty()) result[resultPointer++] = q.poll();
        for (String digit : digits) result[resultPointer++] = digit;

        return result;
    }
}
