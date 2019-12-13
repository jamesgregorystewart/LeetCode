package LeetCode;

public class SortList {

    public static void main(String[] args) {

    }

    /*
    * Sort a linked list in O(n log n) time using constant space complexity.

    Example 1:

    Input: 4->2->1->3
    Output: 1->2->3->4
    Example 2:

    Input: -1->5->3->4->0
    Output: -1->0->3->4->5
    * */

    public ListNode sortList(ListNode head) {
        return new ListNode(0);
    }

    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }
}

