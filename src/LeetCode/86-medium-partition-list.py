from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a_dummy = ListNode(0)
        a_node = a_dummy
        b_dummy = ListNode(0)
        b_node = b_dummy

        node = head
        while node:
            print(node.val)
            if node.val < x:
                a_node.next = node
                a_node = a_node.next
            else:
                b_node.next = node
                b_node = b_node.next
            node = node.next
        b_node.next = None
        a_node.next = b_dummy.next
        return a_dummy.next
