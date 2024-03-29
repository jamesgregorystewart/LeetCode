# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def doReverse(node: ListNode) -> bool:
            count = 0
            while node and count <= k:
                count += 1
                node = node.next
            return False if count < k else True

        def reverseKNodes(prev: ListNode) -> ListNode:
            iterator = prev.next
            count = 1
            while iterator and iterator.next and count < k:
                temp = iterator.next
                prev.next, iterator.next, temp.next = temp, temp.next, prev.next
                count += 1
            return iterator

        if not head:
            return None
        if k == 1:
            return head
        dummy_head = prev = ListNode(0, head)

        while doReverse(prev.next):
            print("doreverse")
            prev = reverseKNodes(prev)

        return dummy_head.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

cur = l1
while cur:
    print(cur.val)
    cur = cur.next

print("--------")

solution = Solution()
node = solution.reverseKGroup(l1, 2)
while node:
    print(node.val)
    node = node.next
