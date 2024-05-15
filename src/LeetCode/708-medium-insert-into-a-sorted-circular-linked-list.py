# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Optional[Node]", insertVal: int) -> "Node":
        if not head:
            newNode = Node(val=insertVal)
            newNode.next = newNode
            return newNode

        prev = head
        cur = head.next
        max_seen = head
        while True:
            if cur.val >= insertVal and prev.val <= insertVal:
                prev.next = Node(val=insertVal, next=prev.next)
                return head
            max_seen = cur if cur.val >= max_seen.val else max_seen
            prev, cur = cur, cur.next

            if prev == head:
                break

        max_seen.next = Node(val=insertVal, next=max_seen.next)
        return head
