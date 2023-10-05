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
        answer = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            answer.extend([node.val, node.left != None, node.right != None])
        return " ".join(answer)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        data = data.split()
        i = 0
        queue = collections.deque([TreeNode(None)])
        while i < len(data):
            node = queue.popleft()
            val, left, right = int(data[i]), bool(data[i + 1]), bool(data[i + 2])
            if left:
                node.left = TreeNode(None)
                queue.append(node.left)
            if right:
                node.right = TreeNode(None)
                queue.append(node.right)

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))