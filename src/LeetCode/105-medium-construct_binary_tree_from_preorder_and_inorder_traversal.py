from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         inorder_to_idx = {data: i for i, data in enumerate(inorder)}
#         def helper(preorder_start, preorder_end, inorder_start, inorder_end) -> TreeNode | None:
#             if preorder_end <= preorder_start or inorder_end <= inorder_start:
#                 return None
#
#             return TreeNode(
#                     val=preorder[preorder_start],
#                     left=helper(
#                         preorder_start + 1,
#                         preorder_start + 1 + inorder_to_idx[preorder[preorder_start]] - inorder_start,
#                         inorder_start,
#                         inorder_to_idx[preorder[preorder_start]]),
#                     right=helper(
#                         preorder_start + 1 + inorder_to_idx[preorder[preorder_start]] - inorder_start,
#                         preorder_end,
#                         inorder_to_idx[preorder[preorder_start]] + 1,
#                         inorder_end))
#
#         return helper(0, len(preorder), 0, len(inorder))


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {data: i for i, data in enumerate(inorder)}

        def helper(
            preorder_start, preorder_end, inorder_start, inorder_end
        ) -> Optional[TreeNode]:
            if preorder_start >= preorder_end or inorder_start >= inorder_end:
                return None
            root_val = preorder[preorder_start]
            root_idx = inorder_idx[root_val]
            # ending indices are exclusive
            return TreeNode(
                val=root_val,
                left=helper(
                    preorder_start=preorder_start + 1,
                    preorder_end=preorder_start + root_idx + 1 - inorder_start,
                    inorder_start=inorder_start,
                    inorder_end=root_idx,
                ),
                right=helper(
                    preorder_start=preorder_start + root_idx - inorder_start + 1,
                    preorder_end=preorder_end,
                    inorder_start=root_idx + 1,
                    inorder_end=inorder_end,
                ),
            )

        return helper(0, len(preorder), 0, len(inorder))
