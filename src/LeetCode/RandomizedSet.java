package LeetCode;

import java.util.*;

public class RandomizedSet {

    public static void main(String[] args) {
        RandomizedSet randomizedSet = new RandomizedSet();
        System.out.println(randomizedSet.insert(1));
        System.out.println(randomizedSet.remove(2));
        System.out.println(randomizedSet.insert(2));
        System.out.println(randomizedSet.getRandom());
        System.out.println(randomizedSet.remove(1));
        System.out.println(randomizedSet.insert(2));
        System.out.println(randomizedSet.getRandom());
    }

    List<Integer> list;
    Map<Integer, Integer> map;
    Random selector = new Random();

    /** Initialize your data structure here. */
    public RandomizedSet() {
        list = new ArrayList<>(); // the list we will get random from
        map = new HashMap<>(); // integer to its index
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val)) return false;
        list.add(list.size(), val);
        map.put(val, list.size()-1);

        return true;
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (!map.containsKey(val)) return false;

        /*
        * replace the last element in the list with the element to be removed and update the moved
        * val with its new index to maintain the accurate val-index relationship between the map and
        * the list
        * */
        int idx = map.get(val); // the index of the value to be removed
        int lastElement = list.get(list.size()-1); // overwrite index of val to be removed with val at end of list

        //overwrite the index in the array
        list.set(idx, lastElement); //replace the value at the end of the arraylist
        map.put(lastElement, idx); //update the index of the value we overwrote with

        list.remove(list.size()-1); //remove the relocated value from end of list
        map.remove(val); //remove val from the map

        return true;
    }

    /** Get a random element from the set. */
    public int getRandom() {
        //generate a val in the range of 0 - list.size() and return the val at that index

        return list.get(selector.nextInt(list.size()));
    }
}
