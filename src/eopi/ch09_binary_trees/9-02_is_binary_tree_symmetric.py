from binary_tree_node import BinaryTreeNode


def is_binary_tree_symmetric(node: BinaryTreeNode) -> bool:
    def check_symmetric(subtree_0, subtree_1) -> bool:
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data and
                    check_symmetric(subtree_0.left, subtree_1.right) and
                    check_symmetric(subtree_0.right, subtree_1.left))
        return False

    return not node or check_symmetric(node.left, node.right)


node1 = BinaryTreeNode(data=1)
node0 = BinaryTreeNode(data=0)
node2 = BinaryTreeNode(data=0)
node1.left = node0
node1.right = node2
node0.right = BinaryTreeNode(data = 3)
node2.left = BinaryTreeNode(data = 3)

print(is_binary_tree_symmetric(node1))
