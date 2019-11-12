package LeetCode;

import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.LinkedHashMap;

public class LRUCache {

    public static void main(String[] args) {

    }


    private HashMap<Integer, Integer> map;
    private ArrayDeque<Integer> q;
    private int totalCapacity;
    private int curCapacity;

    public LRUCache(int capacity) {
        this.map = new HashMap<>(capacity);
        this.q = new ArrayDeque<>(capacity);
        totalCapacity = capacity;
        this.curCapacity = 0;
    }

    public int get(int key) {
        if (map.containsKey(key)) {
            q.remove(key);
            q.offerFirst(key);
            return map.get(key);
        }
        return -1;
    }

    public void put(int key, int value) {
        if (map.containsKey(key)) {
            q.remove(key);
            q.offerFirst(key);
        }
        else if (curCapacity < totalCapacity) {
            curCapacity++;
            q.offerFirst(key);
        }
        else if (!q.isEmpty()){
            int removed = q.pollLast();
            map.remove(removed);
            q.offerFirst(key);
        }
        map.put(key, value);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */