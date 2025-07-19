# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrderBFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        if root:
            q.append(root)
        
        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(level)
        
        return res

    def levelOrderDFS(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(root, level):
            if not root:
                return 0
            
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        return res