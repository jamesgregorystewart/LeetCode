from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {data: i for i, data in enumerate(inorder)}

        def helper(
            inorder_start, inorder_end, postorder_start, postorder_end
        ) -> Optional[TreeNode]:
            if inorder_start > inorder_end or postorder_start > postorder_end:
                return None

            root_val = postorder[postorder_end]
            root_index = inorder_idx[root_val]

            return TreeNode(
                val=postorder[postorder_end],
                left=helper(
                    inorder_start=inorder_start,
                    inorder_end=root_index - 1,
                    postorder_start=postorder_start,
                    postorder_end=postorder_start + root_index - inorder_start - 1,
                ),
                right=helper(
                    inorder_start=root_index + 1,
                    inorder_end=inorder_end,
                    postorder_start=postorder_start + root_index - inorder_start,
                    postorder_end=postorder_end - 1,
                ),
            )

        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
