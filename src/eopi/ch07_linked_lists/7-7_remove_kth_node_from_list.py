""" Remove kth Last Element from List """

"""
Idea:
    - single pass solution with two iterators, one k steps ahead of the other
"""

from util.models import *

def remove_kth_element(L: ListNode, k: int) -> None:
    l = r = L
    for _ in range(k):
        r = r.next
    while r.next:
        l, r = l.next, r.next
    l.next = l.next.next

L = LinkedList()
L.append_values(list(range(10)))
remove_kth_element(L.head, 2)
L.print_list()

