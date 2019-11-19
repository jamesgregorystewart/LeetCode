package LeetCode;

import java.util.LinkedHashMap;
import java.util.Map;

class LoggerRateLimiter {

    private LinkedHashMap<String, Integer> map;
    private int lastSecond;

    /** Initialize your data structure here. */
    public LoggerRateLimiter() {
        lastSecond = 0;
        map = new LinkedHashMap<>(10, 0.75f, true) {
            @Override
            protected boolean removeEldestEntry(Map.Entry<String, Integer> eldest) {
                return lastSecond - eldest.getValue() > 10;
            }
        };
    }

    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
     If this method returns false, the message will not be printed.
     The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        lastSecond = timestamp;

        return false;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */
