""" Merge Two Linked Lists """

"""
Time: O(n)
Space: O(1)
"""

from util.models import *

def merge_two_singly_linked_lists(L1: ListNode, L2: ListNode) -> ListNode:
    dummy_head = tail = ListNode()
    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    # appends the remaining L1 or L2 
    tail.next = L1 or L2
    return dummy_head.next


l0, l1 = LinkedList(), LinkedList()
l0.append(0)
l0.append(2)
l0.append(4)
l1.append(1)
l1.append(3)
l1.append(5)

# l0.print_list()
# l1.print_list()

print(merge_two_singly_linked_lists(l0.head, l1.head).data)
