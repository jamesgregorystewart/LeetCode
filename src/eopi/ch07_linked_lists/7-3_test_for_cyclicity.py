""" Test for Cyclicity """


"""
Time: O(n) Linear with size of input
Space: O(1)
"""

from util.models import *

def is_list_cyclic(L: ListNode) -> bool:
    dummy_head = ListNode(0, L)
    s_cur, f_cur = L.next, L.next.next

    while s_cur.next and f_cur.next.next:
        if s_cur == f_cur:
            return True
        s_cur, f_cur = s_cur.next, f_cur.next.next

    return False

L = LinkedList()
L.append_values(list(range(20)))

cycle_start = L.head
for _ in range(4):
    cyclee_start = cycle_start.next

cycle_end = cycle_start
while cycle_end.next:
    cycle_end = cycle_end.next

cycle_end.next = cycle_start


print(is_list_cyclic(L.head))

L2 = LinkedList()
L2.append_values(list(range(20)))
print(is_list_cyclic(L2.head))
