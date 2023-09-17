""" Even-Odd Merge of Singly Linked List """
 
"""
Idea:
    - even and odd pointers, maintain odd_head for reference at end

Time: O(n)
Space: O(1)
"""

from util.models import *

def even_odd_merge(L: ListNode) -> None:
    odd_head, even, odd = ListNode(0, L.next), L, L.next

    while odd.next:
        even.next = odd.next
        even = even.next
        if not even.next:
            break
        odd.next = even.next
        odd = odd.next

    odd.next = None
    even.next = odd_head.next

L = LinkedList()
L.append_values(list(range(6)))
L.print_list()

even_odd_merge(L.head)
L.print_list()
