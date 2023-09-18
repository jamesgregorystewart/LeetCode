# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#  
#
# Example 1:
#
#
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
#
# Input: list1 = [], list2 = []
# Output: []
# Example 3:
#
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
#
# Constraints:
#
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

from typing import Optional
from util.models import *

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, None)
        prev = dummy_head
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next, list1 = list1, list1.next
            else:
                prev.next, list2 = list2, list2.next
            prev = prev.next
        prev.next = list1 if list1 else list2

        return dummy_head.next


list1 = LinkedList()
list1.append_values(range(7))
list2 = LinkedList()
list2.append_values(range(0))

solution = Solution()
res = solution.mergeTwoLists(list1.head, list2.head)
while res:
    print(res.val)
    res = res.next

