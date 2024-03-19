# Linked Lists

## Top Tricks for solving
- Reversing linked Lists
- Two pointer approaches
- Merging linked Lists
- Use of dummy nodes to maintain reference
- Always examine if the node is null before you call the next field
- When appending linked lists together make sure to set the next field of the last element of the appended list to None to prevent cycles; this is particularly common on problems wherein you are rearranging a linked list by creating multiple lists and then concatenating them.

## Thoughts

Things to keep in mind with respect to solving linked list problems:
- fast and slow pointers for cycle detection
- interleaving new nodes with old nodes to clone a structure; to be unweaved after the fact
- use of pointers such as dummy_head to hold reference to the start of a list
- use of three pointers to reverse a list -> prev, cur, next -- 
    prev, cur, cur.next = cur, next, prev; next = next.next

Problems:
- [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/description/?envType=study-plan-v2&envId=top-interview-150)
- [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150)


Proper way to reverse a segment of a linked list. Move prev to the first node not to be reversed if it is to be a subset of a linked list:
```python
dummy = ListNode(0, head)
prev = dummy
iterator = prev.next
while iterator and iterator.next:
    temp = iterator.next
    prev.next, iterator.next, temp.next = temp, temp.next, prev.next

return dummy.next
```
