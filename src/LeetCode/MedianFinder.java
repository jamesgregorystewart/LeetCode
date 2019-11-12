package LeetCode;

import java.util.PriorityQueue;

public class MedianFinder {

    private PriorityQueue<Integer> lowerHalf;
    private PriorityQueue<Integer> upperHalf;

    public MedianFinder() {
        lowerHalf = new PriorityQueue<>(1, (a,b) -> {return a > b ? a : b;});
        upperHalf = new PriorityQueue<>();
    }

    public void addNum(int num) {
        lowerHalf.offer(num);
        upperHalf.offer(lowerHalf.poll());
        if (lowerHalf.size() < upperHalf.size())
            lowerHalf.offer(upperHalf.poll());
    }

    public double findMedian() {
        return (double)lowerHalf.size() > upperHalf.size() ? lowerHalf.peek() : (upperHalf.peek() + lowerHalf.peek()) / 2.0;
    }
}
