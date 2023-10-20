# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node, string) -> str:
            if node is None:
                string += "null," 
            else:
                string += str(node.val) + ","
                string = helper(node.left, string)
                string = helper(node.right, string)
            return string
        return helper(root, "")


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(node_list) -> TreeNode:
            if node_list[0] == "null":
                node_list.pop(0)
                return None
            root = TreeNode(node_list.pop(0))
            root.left = helper(node_list)
            root.right = helper(node_list)
            return root
        
        print(data)
        tree_data = data.split(",")
        return helper(tree_data)



# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

t0 = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
t3 = TreeNode(4)
t4 = TreeNode(5)
t5 = TreeNode(6)
t6 = TreeNode(7)
t0.left = t1
t0.right = t2
t2.left = t3
t2.right = t4
t3.left = t5
t3.right = t6

codec = Codec()
# print(codec.serialize(t0))
print(codec.deserialize(codec.serialize(t0)))
