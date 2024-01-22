# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
# Example 2:
#
# Input: root = []
# Output: []
#  
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 212 - 1].
# -1000 <= Node.val <= 1000


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from typing import Tuple
import collections

# BFS Solution
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root

        queue = collections.deque()
        queue.append((root, 0))
        prev = None

        while queue:
            node = queue.popleft()
            if prev and prev[1] == node[1]:
                prev[0].next = node[0]
            if node[0].left:
                queue.append((node[0].left, node[1]+1))
            if node[0].right:
                queue.append((node[0].right, node[1]+1))
            prev = node
        return root


# O(1) space; Recursive
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        self.connect_nodes(root.left, root.right)
        return root

    def connect_nodes(self, A, B):
        if A and B:
            A.next = B
            self.connect_nodes(A.left, A.right)
            self.connect_nodes(A.right, B.left)
            self.connect_nodes(B.left, B.right)
