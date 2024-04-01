from typing import Optional
from collections import defaultdict


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counts = defaultdict(int)
        node = head
        while node:
            counts[node.val] += 1
            node = node.next

        dummy = ListNode(0)
        prev = dummy
        for _, v in counts.items():
            prev.next = ListNode(v)
            prev = prev.next

        return dummy.next
