package LeetCode;

import java.util.HashMap;
import java.util.Map;

public class MinWindowSubstring {
    public String minWindow(String s, String t) {
        Map<Character, Integer> searchMap = new HashMap<>(); //maintain counts of each of the characters in the search string
        Map<Character, Integer> windowMap = new HashMap<>();
        int fP = 0;
        int bP = 0;
        String minString = "";

        //Load up the searchMap
        for (int i = 0; i < t.length();  i++) {
            if (!searchMap.containsKey(t.charAt(i))) searchMap.put(t.charAt(i), 1); //put if it does not exist
            else searchMap.put(t.charAt(i), searchMap.get(t.charAt(i))+1); //else increment the count at that location
        }

        boolean moveFront = false;
        //Now we need to find the smallest window that has the searchMap inside it
        while(fP <= bP) {
            if (moveFront) {
                //first check to see if we CAN move front pointer
                if (searchMap.containsKey(s.charAt(fP)) && windowMap.get(s.charAt(fP)) <= searchMap.get(s.charAt(fP))) {
                    moveFront = false;

                }
                //if so, move pointer, update windowMap, and update minString if possible
                else {
                    windowMap.put(s.charAt(fP), windowMap.get(fP)-1);
                    if (minString.equals("") || minString.length() > bP-fP) minString = s.substring(fP, bP+1);
                    fP++;
                }
            } else { //move back pointer
                //if at the end or windowMap has all the min counts needed to move front then move Front
                if (bP > s.length()-1 || shouldSwitchToFront(windowMap, searchMap)) {
                    moveFront = true;
                    if (minString.equals("") || minString.length() > bP-fP) minString = s.substring(fP, bP+1);
                }
                else {
                    if (!windowMap.containsKey(s.charAt(bP))) {
                        windowMap.put(s.charAt(bP), 1);
                    } else {
                        windowMap.put(s.charAt(bP), windowMap.get(s.charAt(bP)) + 1);
                    }
                    bP++;
                }
            }
        }
        return minString;
    }

    public boolean shouldSwitchToFront(Map<Character, Integer> windowMap, Map<Character, Integer> searchMap) {
        for (Character key : searchMap.keySet()) {
            if (!windowMap.containsKey(key) || windowMap.get(key) < searchMap.get(key)) return false;
        }
        return true;
    }
}
