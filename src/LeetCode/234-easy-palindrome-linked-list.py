# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return None

        dummy_head = ListNode(0, head)
        length = -1
        node = dummy_head
        while node:
            node = node.next
            length += 1
        print(length)

        # put a pointer at the half way point; reverse first half as we go along
        prev = dummy_head
        node = prev.next
        i = 0
        while node and i < length // 2:
            next = node.next
            node.next, prev = prev, node
            node = next
            i += 1
        reverse_node = prev
        if length % 2:
            node = node.next

        while reverse_node and node:
            if reverse_node.val != node.val:
                return False
            reverse_node, node = reverse_node.next, node.next
        return True
