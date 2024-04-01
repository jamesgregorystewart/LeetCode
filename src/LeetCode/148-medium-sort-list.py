from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time: O(N^2); Space: O(1)     TLE
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#
#         dummy = ListNode(0, head)
#         prev = dummy
#         pt, it = prev, prev.next
#         while prev and prev.next:
#             if it and it.val < prev.next.val:
#                 temp = it.next
#                 pt.next = temp
#                 it.next = prev.next
#                 prev.next = it
#                 it = temp
#             elif it:
#                 pt = it
#                 it = it.next
#             else:
#                 prev = prev.next
#                 pt, it = prev, prev.next
#         return dummy.next


# O(Nlog(N)) / O(log(N))   Top-Down Mergesort
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, left, right) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
                tail = tail.next
            else:
                tail.next = right
                right = right.next
                tail = tail.next
        tail.next = left if left else right
        return dummy.next

    def getMid(self, head) -> Optional[ListNode]:
        midPrev = None
        while head and head.next:
            midPrev = head if not midPrev else midPrev.next
            head = head.next.next
        mid = midPrev.next
        midPrev.next = None
        return mid
