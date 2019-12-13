package LeetCode;

public class IntersectionOfTwoLinkedLists {

    /*
    * Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.
    * */

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int diff = 0;
        int a_length = 0;
        int b_length = 0;

        ListNode dummyA = headA;
        ListNode dummyB = headB;

        while (dummyA.next != null) {
            dummyA = dummyA.next;
            a_length++;
        }

        while (dummyB.next != null) {
            dummyB = dummyB.next;
            b_length++;
        }
        diff = Math.abs(a_length - b_length);
        if (a_length > b_length) {
            while (diff != 0) {
                headA = headA.next;
                diff--;
            }
        } else {
            while (diff != 0) {
                headB = headB.next;
                diff--;
            }
        }

        while (headA != null && headB != null) {
            if (headA.val == headB.val) return headA;
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }

    class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }
}
