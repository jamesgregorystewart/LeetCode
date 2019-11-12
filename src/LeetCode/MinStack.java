package LeetCode;

import java.util.Comparator;
import java.util.Objects;
import java.util.PriorityQueue;
import java.util.Stack;

public class MinStack {

    /*
    * Maintain a variable identifying the global min
    * -> Every node points to the next greatest (i.e. the previous min before it)
    * -> biggest node points to null
    *
    * -> Use a map of val -> StackNode to
    * */

    /** initialize your data structure here. */
    Stack<StackNode> stack;
    PriorityQueue<StackNode> q;

    public MinStack() {
        stack = new Stack<>();
        q = new PriorityQueue<>();
    }

    public void push(int x) {
        StackNode newNode = new StackNode(x);
        q.offer(newNode);
        stack.push(newNode);
    }

    public void pop() {
        StackNode removed = stack.pop();
        q.remove(removed);
    }

    public int top() {
        return stack.peek().val;
    }

    public int getMin() {
        return q.peek().val;
    }

    class StackNode implements Comparable<StackNode>{
        int val;
        StackNode next;

        public StackNode(int val) {
            this.val = val;
        }

        @Override
        public int compareTo(StackNode node) {
            return Integer.compare(this.val, node.val);
        }
    }
}
