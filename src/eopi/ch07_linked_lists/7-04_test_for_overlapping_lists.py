""" Test for Overlapping Lists """

"""
Idea:
    1) Get length of each list
    2) Take difference of lengths
    3) Move pointer along longer list for difference length
    4) Move pointer in each list in tandem until they either reach end or meet on a node

Time: O(n)
Space: O(1)
"""

from util.models import *

def get_overlapping_node(L1: ListNode, L2: ListNode) -> ListNode | None:
    p1, p2 = L1, L2
    p1_length, p2_length = 1, 1
    
    # 1) Get lengths of lists
    while p1 or p2:
        if p1:
            p1, p1_length = p1.next, p1_length + 1
        if p2:
            p2, p2_length = p2.next, p2_length + 1

    # 2) Set up runners
    (long_runner, short_runner) = L1, L2 if p1_length > p2_length else (L2, L1)
    for _ in range(abs(p1_length-p2_length)):
        long_runner = long_runner.next

    # 3) Run the runners
    while long_runner and short_runner:
        if long_runner == short_runner:
            return short_runner
        long_runner, short_runner = long_runner.next, short_runner.next

    return None


L1 = LinkedList()
L2 = LinkedList()
L1.append_values(list(range(3)))
L2.append_values(list(range(4,10)))

n1 = L1.head
while n1.next:
    n1 = n1.next
n1.next = L2.head

# L1.print_list()
# L2.print_list()

print(get_overlapping_node(L1.head, L2.head).data)
