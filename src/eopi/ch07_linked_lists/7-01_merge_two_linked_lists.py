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


"""
Doubly Linked List
"""

def merge_two_doubly_linked_lists(L1: ListNode, L2: ListNode) -> ListNode:
    dummyhead = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            L1.prev, tail.next, L1 = tail, L1, L1.next
        else:
            L2.prev, tail.next, L2 = tail, L2, L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummyhead.next

L1, L2  = DoublyLinkedList(), DoublyLinkedList()
L1.append_values([0,2,4])
L2.append_values([1,3,5])
merge_two_doubly_linked_lists(L1=L1.head, L2=L2.head)

if L1.head.data < L2.head.data:
    L1.print_list()
else:
    L2.print_list()
