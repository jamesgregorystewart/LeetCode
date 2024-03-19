class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        cur = head
        # interleave new nodes with existing nodes
        while cur:
            cur.next, temp = Node(cur.val, None, cur.random), cur.next
            cur.next.next = temp
            cur = temp

        # unweave the nodes
        cur = head.next
        while cur:
            cur.random = cur.random.next if cur.random is not None else None
            cur.next = cur.next.next if cur.next is not None else None
            cur = cur.next

        return head.next
