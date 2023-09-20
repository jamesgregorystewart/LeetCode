""" 23. Hard -- Merge K Sorted Lists """

# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.G
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
#  
#
# Example 1:
#
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
# Example 2:
#
# Input: lists = []
# Output: []
# Example 3:
#
# Input: lists = [[]]
# Output: []
#  
#
# Constraints:
#
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Idea:
    - iteratively merge the lists into the first list
    - maintain the new head between merges
"""

from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeLists(L1: ListNode, L2: ListNode) -> ListNode:
            dummy_head = prev = ListNode(0, L1)
            it1, it2 = L1, L2
            while it1 and it2:
                if it1.val > it2.val:
                    prev.next, it2.next, it2 = it2, it1, it2.next
                    prev = prev.next
                else:
                    it1, prev = it1.next, prev.next

            if it2:
                prev.next = it2
            
            return dummy_head
        
        head = ListNode(0, lists[0])
        for i in range(1, len(lists)):
            head = mergeLists(head.next, lists[i])

        return head.next

