"""
Tips, tricks, paradigms, and useful functions and patterns for reference in solving Linked List Problems
"""

"""
Notes:
    - Maintain a dummy_head which is a new node which points to the first node of a provided list
    - Pointers are key; When doing reversals you may need a few pointers, one to maintain you original starting point,
        another to iterate, and a temp to maintain reference to a node that could otherwise be dereferenced. E.g. 7.2
"""

# Node model
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Search in a List
def search_list(L: ListNode, key: int) -> ListNode:
    while L and L.data != key:
        L = L.next
    # If key was not present in the list, L will have become null.
    return L


# Insert a Node after a specified Node
def insert_after(node: ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node


# Delete a Node
def delete_after(node: ListNode) -> None:
    node.next = node.next.next
