from binary_tree_node import BinaryTreeNode
from collections import namedtuple


def is_binary_tree_height_balanced(node: BinaryTreeNode) -> bool:
    BalancedTreeNode = namedtuple("BalancedTreeNode", ["balanced", "height"])

    def check_balanced(node: BinaryTreeNode) -> int:
        if not node:
            return BalancedTreeNode(True, -1)

        left_result = check_balanced(node.left)
        if not left_result.balanced:
            return left_result

        right_result = check_balanced(node.right)
        if not right_result.balanced:
            return right_result

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedTreeNode(is_balanced, height)

    return check_balanced(node).balanced
    

node1 = BinaryTreeNode(data=1)
node0 = BinaryTreeNode(data=0)
node2 = BinaryTreeNode(data=2)
node1.left = node0
node0.right = node2
print(is_binary_tree_height_balanced(node1))
