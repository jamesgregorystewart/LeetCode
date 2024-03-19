from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode(0, head)
        node = dummy
        length = 0
        while node.next:
            node = node.next
            length += 1
        k = k % length
        if k == 0:
            return head

        slow, fast = dummy, dummy
        i = 0
        while fast.next and i < k:
            fast = fast.next
            i += 1

        while fast.next:
            slow, fast = slow.next, fast.next

        dummy.next, fast.next, slow.next = slow.next, dummy.next, fast.next
        return dummy.next
