class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        possible_subtrees = []
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        def find_subtrees(node, possible_subtrees, target) -> None:
            if not node:
                return
            if node.val == target.val:
                possible_subtrees.append(node)
            find_subtrees(node.left, possible_subtrees, target)
            find_subtrees(node.right, possible_subtrees, target)
        find_subtrees(root, possible_subtrees, subRoot)

        def compare_trees(tree0, tree1) -> bool:
            if not tree0 and not tree1:
                return True
            if not tree0 or not tree1:
                return False
            return tree0.val == tree1.val and (compare_trees(tree0.left, tree1.left) and 
                                               compare_trees(tree0.right, tree1.right))

        while possible_subtrees:
            node0 = possible_subtrees.pop()
            if compare_trees(node0, subRoot):
                return True

        return False
