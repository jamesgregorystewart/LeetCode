package LeetCode;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class FreqStack {

    Map<Integer, Stack<Integer>> stacks;
    Map<Integer, Integer> freq;
    int maxFreq;

    public FreqStack() {
        stacks = new HashMap<>();
        freq = new HashMap<>();
        maxFreq = 0;
    }

    public void push(int x) {
        //update freq
        int x_freq = freq.getOrDefault(x, 0) + 1;
        freq.put(x, x_freq);

        //update stacks
        stacks.putIfAbsent(x_freq, new Stack<>());
        stacks.get(x_freq).push(x);

        //update maxfreq
        maxFreq = Math.max(x_freq, maxFreq);
    }

    public int pop() {
        int result = stacks.get(maxFreq).pop();
        freq.put(result, freq.get(result) - 1);
        if (stacks.get(maxFreq).isEmpty()) maxFreq--;
        return result;
    }
}
/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */