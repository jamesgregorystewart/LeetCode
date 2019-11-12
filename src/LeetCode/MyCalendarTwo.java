package LeetCode;

class MyCalendarTwo {

    /*MEMORY LIMIT EXCEEDED*/

    int[] bookings;

    public MyCalendarTwo() {
        bookings = new int[1000000001];
    }

    public boolean book(int start, int end) {
        for (int i = start; i <=end; i++) {
            if (bookings[i] == 2) return false;
            bookings[i]++;
        }
        return true;
    }
}
/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */