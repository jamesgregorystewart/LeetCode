""" Add List-Based Integers """

"""
Given two lists representing integeers in reverse order (LSD comes first); return a list representing their sum

"""

"""
Idea:
    - 

Time: O(n)
Space: O(1)
"""

from util.models import *

def add_lists(L1: ListNode, L2: ListNode) -> ListNode:
    dummy_head = ListNode(0, L1)
    carry = 0
    while L1.next and L2.next:
        L1.data += L2.data + carry
        carry = L1.data // 10
        L1.data %= 10
        L1, L2 = L1.next, L2.next
    L1.data += L2.data + carry
    carry = L1.data // 10
    L1.data %= 10

    if not L1.next and not L2.next:
        L1.next = ListNode(carry, None)
        return dummy_head.next

    while L1.next or L2.next:
        if L1.next:
            L1 = L1.next
            L1.data += carry
            carry = L1.data // 10
            L1.data %= 10
        else:
            L2 = L2.next
            L1.next = ListNode(L2.data, None)
            L1 = L1.next
            L1.data += carry
            carry = L1.data // 10
            L1.data %= 10

    if L1:
        L1.data += carry
        carry = L1.data // 10
        L1.data %= 10
    else:
        L1.next = ListNode(L2.data, None)
        L1 = L1.next
        L1.data += carry
        carry = L1.data // 10
        L1.data %= 10
    if carry:
        L1.next = ListNode(carry, None)


    return dummy_head.next

L1 = LinkedList()
L2 = LinkedList()

L1.append(3)
L2.append(7)
L2.append(0)
L2.append(9)

add_lists(L1.head, L2.head)

L1.print_list()
