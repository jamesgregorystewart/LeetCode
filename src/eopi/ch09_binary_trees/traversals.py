
from binary_tree_node import BinaryTreeNode


"""
Preorder
"""
def preorder_traverse(node: BinaryTreeNode) -> None:
    print("Preorder: %s"  % node.data)
    if node.left:
        preorder_traverse(node.left)
    if node.right:
        preorder_traverse(node.right)


"""
Inorder
"""
def inorder_traverse(node: BinaryTreeNode) -> None:
    if node.left:
        inorder_traverse(node.left)
    print("Inorder: %s" % node.data)
    if node.right:
        inorder_traverse(node.right)


"""
Postorder
"""
def postorder_traverse(node: BinaryTreeNode) -> None:
    if node.left:
        postorder_traverse(node.left)
    if node.right:
        postorder_traverse(node.right)
    print("Postorder: %s" % node.data)



node1 = BinaryTreeNode(data=1)
node0 = BinaryTreeNode(data=0)
node2 = BinaryTreeNode(data=2)
node1.left = node0
node1.right = node2
print(preorder_traverse(node1))
print(inorder_traverse(node1))
print(postorder_traverse(node1))
