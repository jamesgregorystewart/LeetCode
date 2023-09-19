# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
Idea:
    - Use grade-school mathematics to add each integer, tracking carry
Time: O(max(n,m))
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2
        
        dummy_head, carry = ListNode(0, l1), 0

        while l1.next:
            l1.val += l2.val + carry if l2 else carry
            carry = l1.val // 10
            l1.val %= 10
            l1 = l1.next
            if l2.next:
                l2 = l2.next

        while l2.next:
            l1.val += l2.val + carry
            carry = l1.val // 10
            l1.val %= 10
            if not l1.next:
                l1.next = ListNode(0, None)
            l1, l2 = l1.next, l2.next

        if l2 or carry:
            l1.val += l2.val + carry if l2 else carry
            carry = l1.val // 10
            l1.val %= 10

        if carry:
            l1.next = ListNode(carry, None)

