""" Test for Cyclicity """


"""
Time: O(n) Linear with size of input
Space: O(1)
"""

from util.models import *

def find_start_of_cycle(L: ListNode) -> None | ListNode:
    dummy_head = ListNode(0, L)
    s_cur, f_cur = L.next, L.next.next
    
    # Find Cycle
    intercept_node = None
    while s_cur.next and f_cur.next.next:
        if s_cur == f_cur:
            intercept_node = s_cur
            break
        s_cur, f_cur = s_cur.next, f_cur.next.next

    if not intercept_node:
        return None

    # Find Cycle Length
    s_cur, cycle_length = s_cur.next, 1
    while s_cur != intercept_node:
        s_cur, cycle_length = s_cur.next, cycle_length + 1

    back_node = front_node = L
    for _ in range(cycle_length):
        front_node = front_node.next

    while back_node != front_node:
        back_node, front_node = back_node.next, front_node.next

    return back_node


L = LinkedList()
L.append_values(list(range(20)))

cycle_start = L.head
for _ in range(4):
    cycle_start = cycle_start.next

cycle_end = cycle_start
while cycle_end.next:
    cycle_end = cycle_end.next

cycle_end.next = cycle_start

print(find_start_of_cycle(L.head).data)

# L2 = LinkedList()
# L2.append_values(list(range(20)))
# print(find_start_of_cycle(L2.head).data)
