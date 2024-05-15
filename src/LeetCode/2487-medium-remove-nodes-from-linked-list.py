from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(val=float("inf"), next=head)
        cur = dummyhead
        stack = [dummyhead]
        while (cur := cur.next) is not None:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack[-1].next = cur
            stack.append(cur)
        return stack[0].next
