from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        answer = []
        queue_1, queue_2 = deque(), deque()
        queue_1.append(root)
        while queue_1:
            node = queue_1.popleft()
            if node.left:
                queue_2.append(node.left)
            if node.right:
                queue_2.append(node.right)
            if not queue_1:
                queue_1, queue_2 = queue_2, deque()
                answer.append(node.val)
        return answer

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
print(Solution().rightSideView(root))
        