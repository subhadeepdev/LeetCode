import collections

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
        if not root:
            return ""
        nodeList = []
        queue = collections.deque([root])
        while queue:
            left, right = 0, 0
            node = queue.popleft()
            if node.left:
                left = 1
                queue.append(node.left)
            if node.right:
                right = 1
                queue.append(node.right)
            nodeList.extend([node.val, left, right])
        return " ".join(str(item) for item in nodeList)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        data = data.split()
        i, root = 0, TreeNode(None)
        queue = collections.deque([root])
        while i < len(data):
            node = queue.popleft()
            node.val, left, right = int(data[i]), int(data[i + 1]), int(data[i + 2])
            i += 3
            if left:
                node.left = TreeNode(None)
                queue.append(node.left)
            if right:
                node.right = TreeNode(None)
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))