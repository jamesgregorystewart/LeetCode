# Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#  
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:
#
# Input: head = [1], n = 1
# Output: []
# Example 3:
#
# Input: head = [1,2], n = 1
# Output: [1]
#  
#
# Constraints:
#
# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#  
#
# Follow up: Could you do this in one pass?

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        seeker = runner = dummy_head = ListNode(0, head)
        
        # put runner n places ahead of seeker
        for _ in range(n):
            runner = runner.next
        
        # run the seeker and runner till runner hits the end so seeker is n from end
        while runner.next:
            runner, seeker = runner.next, seeker.next

        # Delete the node after seeker to delete the nth from last node
        seeker.next = seeker.next.next

        return dummy_head.next 
