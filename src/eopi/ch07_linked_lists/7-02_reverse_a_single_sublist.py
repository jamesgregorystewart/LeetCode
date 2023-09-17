""" Reverse a Single Sublist """

from util.models import *

def reverse_a_single_sublist(L: ListNode, s: int, f: int) -> None:
    dummy_head = sublist_head = ListNode(0, L)
    for _ in range(1, s):
        sublist_head = sublist_head.next

    # Reverse the sublist
    sublist_iter = sublist_head.next
    for _ in range(f - s):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
    return dummy_head.next


L = LinkedList()
L.append_values([2,3,5,7,11])
reverse_a_single_sublist(L.head, 2, 4)
L.print_list()
