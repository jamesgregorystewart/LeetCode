# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_to_idx = {data: i for i, data in enumerate(inorder)}
        def helper(preorder_start, preorder_end, inorder_start, inorder_end) -> TreeNode | None:
            if preorder_end <= preorder_start or inorder_end <= inorder_start:
                return None

            return TreeNode(
                    val=preorder[preorder_start],
                    left=helper(
                        preorder_start + 1,
                        preorder_start + 1 + inorder_to_idx[preorder[preorder_start]] - inorder_start,
                        inorder_start,
                        inorder_to_idx[preorder[preorder_start]]),
                    right=helper(
                        preorder_start + 1 + inorder_to_idx[preorder[preorder_start]] - inorder_start,
                        preorder_end,
                        inorder_to_idx[preorder[preorder_start]] + 1,
                        inorder_end))

        return helper(0, len(preorder), 0, len(inorder))


