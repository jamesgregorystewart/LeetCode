""" Right Cyclic Shift for Singly Linked List """

"""
Idea:
    - Move pointer to end
    - Assign end.next = head; head.next = None; iterate k - 1 times
"""


from util.models import *

def right_cyclic_shift_list(L: ListNode, k: int) -> ListNode:
    head = tail = L
    n = 0
    while tail.next:
        tail = tail.next
        n += 1
    k %= n # update k to k % n in case k > n to avoid unnecessary shifts

    for _ in range(k):
        new_head = head.next
        tail.next = head
        head.next = None
        head = new_head
        tail = tail.next
    return head

L = LinkedList()
L.append_values(list(range(5)))
L2 = right_cyclic_shift_list(L.head, 3)
node = L2
while node:
    print(node.data)
    node = node.next
