""" Delete a Node from a List """

"""
Time: O(n)
Space: O(1)
"""

def delete_node_from_list(L: ListNode, d: ListNode) -> None:
    iterator = L
    while iterator.next:
        if iterator.next == d:
            iterator.next = d.next
