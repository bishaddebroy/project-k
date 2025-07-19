# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()

        if root:
            q.append(root)
        
        while q:
            q_len = len(q)
            rightnode = 0

            for i in range(q_len):
                node = q.popleft()
                rightnode = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(rightnode)
        
        return res

    def rightSideViewDFS(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root, level):
            if not root:
                return None
            
            if len(res) == level:
                res.append(root.val)
            
            dfs(root.right, level + 1)
            dfs(root.left, level + 1)

        dfs(root, 0)
        return res
        