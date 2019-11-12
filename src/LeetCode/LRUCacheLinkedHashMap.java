package LeetCode;

import java.util.LinkedHashMap;
import java.util.Map;

public class LRUCacheLinkedHashMap extends LinkedHashMap<Integer, Integer> {

    int capacity;

    public LRUCacheLinkedHashMap(int capacity) {
        super(capacity, .75f, true);
        this.capacity = capacity;
    }

    public int get(int key) {
        return super.get(key);
    }

    public void put(int key, int value) {
        super.put(key, value);
    }

    @Override
    protected boolean removeEldestEntry(Map.Entry<Integer, Integer> entry) {
        return super.size() > capacity;
    }
}
