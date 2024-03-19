from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Idea is that prev will sit at the front, pointing at temp over and over. iterator will
iterate through the segment managing references for us to remap as we work through reversing
"""


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        dummy = ListNode(0, head)
        prev = dummy
        while left > 1:
            prev = prev.next
            left, right = left - 1, right - 1

        iterator = prev.next
        while iterator and iterator.next and right > 1:
            temp = iterator.next
            prev.next, iterator.next, temp.next = temp, temp.next, prev.next
            right -= 1

        return dummy.next
