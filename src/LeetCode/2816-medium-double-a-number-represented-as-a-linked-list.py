# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(next=head)
        stack = []

        node = head
        while node:
            stack.append(node)
            node = node.next

        carry = 0
        while stack:
            node = stack.pop()
            temp = (node.val * 2) + carry
            node.val = temp % 10
            carry = temp // 10

        if carry:
            dummyhead.next = ListNode(val=carry, next=head)

        return dummyhead.next
