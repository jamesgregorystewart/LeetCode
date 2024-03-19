# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy_evens = ListNode(0, head)
        dummy_odds = ListNode(0, head)

        node_e = dummy_evens
        node_o = dummy_odds

        i = 1
        node = head
        while node:
            if i % 2:
                node_o.next = node
                node_o = node
            else:
                node_e.next = node
                node_e = node
            node = node.next
            i += 1

        node_e.next = None
        node_o.next = dummy_evens.next
        return dummy_odds.next
