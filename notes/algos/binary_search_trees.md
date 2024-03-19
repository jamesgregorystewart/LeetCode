# Binary Trees

## Why Binary Trees?
You can perform all search, insertion, and deletion operations in O(h) time complexity, even in the worst case. Usually, if you want to store data in order and need several operations, such as search, insertion or deletion at the same time, a BST might be a good choice.

Many can be solved with simple recursive solutions
```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth) -> int:
            if not node:
                return depth
            return max(helper(node.left, depth + 1), helper(node.right, depth + 1))

        return helper(root, 0)
```

## Inorder Successor problem

```python
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left
        return successor
```

## Searching a BST
### Recursive
```python
class Solution {
    public TreeNode searchBST(TreeNode root, int target) {
        if (root == null || root.val == target) {
            return root;
        }
        if (target < root.val) {
            return searchBST(root.left, target);
        }
        return searchBST(root.right, target);
    }
}
```

### Iterative
```python
class Solution {
    public TreeNode searchBST(TreeNode root, int target) {
        TreeNode cur = root;
        while (cur != null && cur.val != target) {
            if (target < cur.val) {
                cur = cur.left;
            } else {
                cur = cur.right;
            }
        }
        return cur;
    }
}
```

## Inserting into a BST
1. Search the left and right subtrees according to the relation of the value of the node and the value of our target node
2. Repeat step 1 until reaching an external node
3. Add the new node as its left or right child depending on the relation of the value of the node and the value of our target node.
```python
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if not root
            return new TreeNode(val);   // return a new node if root is null
        }
        if (root.val < val) {           // insert to the right subtree if val > root->val
            root.right = insertIntoBST(root.right, val);
        } else {                        // insert to the left subtree if val <= root->val
            root.left = insertIntoBST(root.left, val);
        }
        return root;
    }
}
```

## Deleting in a BST
1. If the target node has no child, we can simpoly remove the node.
2. If the target has one child, we can use its child to replace itself.
3. If the target has two children, replace the node with its in-order successor or predecessor node and delete that node.
```python
class Solution:
    def successor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # finds the smallest node greater than root
        node = root.right
        while node and node.left:
            node = node.left
        return node.val

    def predecessor(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # finds the greatest node smaller than root
        node = root.left
        while node and node.right:
            node = node.right
        return node.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val < key:
            # node to delete is in the right subtree
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            # node to delete is in the left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            # delete the node
            if not root.left and not root.right:
                root = None
            elif root.left:
                # if node has left child then we can replace with predecessor
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
            else:
                # else we can replace with successor
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
        return root
```
