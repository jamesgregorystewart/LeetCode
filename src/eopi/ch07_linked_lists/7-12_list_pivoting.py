""" Implement List Pivoting """

"""
Idea: build three separate 'lists' with pointers and tie them together at end

Time: O(n)
Space: O(1)
"""

from util.models import *

def pivot_list(L: ListNode, pivot: int) -> ListNode:
    less_head = less_iterator = ListNode(0, None)
    equal_head = equal_iterator = ListNode(0, None)
    greater_head = greater_iterator = ListNode(0, None)

    while L:
        if L.data < pivot:
            less_iterator.next = L
            less_iterator = less_iterator.next
        elif L.data == pivot:
            equal_iterator.next = L
            equal_iterator = equal_iterator.next
        else:
            greater_iterator.next = L
            greater_iterator = greater_iterator.next
        L = L.next

    greater_iterator.next = None
    equal_iterator.next = greater_head.next
    less_iterator.next = equal_head.next
    return less_head.next

L = LinkedList()
L.append(5)
L.append(4)
L.append(3)
L.append(3)
L.append(6)
L.append(7)
L.append(4)
L2 = pivot_list(L.head, 5)

node = L2
while node:
    print(node.data)
    node = node.next
