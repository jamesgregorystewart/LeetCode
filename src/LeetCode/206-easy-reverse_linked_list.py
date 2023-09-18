# Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#  
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
#
# Input: head = []
# Output: []
#  
#
# Constraints:
#
# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000
#  
#
# Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from util.models import *

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        prev, iterator, temp = None, head, None
        while iterator.next:
            temp, iterator.next = iterator.next, prev
            prev, iterator = iterator, temp
        iterator.next = prev
        return iterator

L = LinkedList()
L.append_values(list(range(1)))
solution = Solution()
L2 = solution.reverseList(L.head)
while L2:
    print(L2.data)
    L2 = L2.next
