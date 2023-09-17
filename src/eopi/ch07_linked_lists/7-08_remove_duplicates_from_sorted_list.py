""" Remove Duplicates from Sorted List """

"""
Idea:
    - two iterators
"""

from util.models import *

def remove_duplicates_from_sorted_list(L: ListNode) -> None:
    l, r = L, L.next
    while r.next:
        if l.data == r.data:
            l.next = r.next
        else:
            l = l.next
        r = r.next

L = LinkedList()
L.append(1)
L.append(1)
L.append(2)
L.append(3)
L.append(3)
L.append(3)
L.append(4)
remove_duplicates_from_sorted_list(L.head)
L.print_list()
    
