# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        slow, fast = head, head
        while slow and slow.next and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow and fast and slow.val == fast.next or slow == fast:
                print("cycle found at %s" % slow.val)
                slow2 = head
                while slow and slow2:
                    if slow.val == slow2.val:
                        return slow
                    slow, slow2 = slow.next, slow2.next
                return None
        return None
